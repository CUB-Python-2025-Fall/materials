import re
from dataclasses import dataclass, field

import nltk.data
from tqdm import tqdm
import spacy
from typing import Set, Generator
from spacy.tokens import Token
from nltk.sentiment import SentimentIntensityAnalyzer


@dataclass(frozen=True)
class Word:
    content: str
    pos_tag: str
    lemma: str | None
    positivity: float
    negativity: float


@dataclass
class POSFrequencyData:
    total: int = 0
    unique: Set[str] = field(default_factory=lambda: set())


@dataclass
class WordData:
    total_word_count: int = 0
    unique_words: Set[str] = field(default_factory=lambda: set())
    pos_frequency_data: dict[str, POSFrequencyData] = field(default_factory=lambda: {})
    longest_noun_word: str = ""
    total_positivity: float = 0
    total_negativity: float = 0

    def __str__(self) -> str:
        result = f"Total words: {self.total_word_count}\n"
        result += f"Unique words: {len(self.unique_words)}\n"
        result += "-----------------\n"
        for pos_tag, data in self.pos_frequency_data.items():
            result += f"{spacy.explain(pos_tag)}: Total {data.total}, Unique {len(data.unique)}\n"
        result += "-----------------\n"
        result += f"Total positivity: {self.total_positivity}, fraction: {self.total_positivity / self.total_word_count:.3f}\n"
        result += f"Total negativity: {self.total_negativity}, fraction: {self.total_negativity / self.total_word_count:.3f}\n"
        result += f"Longest noun ({len(self.longest_noun_word)} chars): {self.longest_noun_word}\n"
        return result


def token_to_word(token: Token, sia: SentimentIntensityAnalyzer) -> Word | None:
    if token.is_punct:
        return None
    polarity_scores = sia.polarity_scores(token.text)
    return Word(
        content=token.text,
        pos_tag=token.pos_,
        lemma=token.lemma_ if not token.is_punct else None,
        positivity=polarity_scores['pos'],
        negativity=polarity_scores['neg']
    )


def enumerate_processed_lines(file_path: str, pbar: bool = False) -> Generator[str, None, None]:
    if pbar:
        with open(file_path, 'r') as f:
            line_count = sum(1 for line in f)

    with open(file_path, 'r') as f:
        line_iterable = tqdm(f, total=line_count) if pbar else f
        for line in line_iterable:
            processed_line = re.sub(r'[^a-zA-Z]', ' ', line)
            yield processed_line


def enumerate_words(
        file_path: str,
        batch_size: int = 1000,
        n_process: int = 4,
        pbar: bool = False
) -> Generator[Word, None, None]:
    nlp = spacy.load("en_core_web_sm")
    sia = SentimentIntensityAnalyzer()

    for doc in nlp.pipe(enumerate_processed_lines(file_path, pbar), batch_size=batch_size, n_process=n_process, disable=['ner']):
        for token in doc:
            word = token_to_word(token, sia)
            if word is not None:
                yield word


def ensure_dependencies() -> None:
    try:
        spacy.load('en_core_web_sm')
    except OSError:
        print("Downloading spaCy model (this may take a while)...")
        spacy.cli.download('en_core_web_sm')
        print('Spacy model downloaded')

    try:
        nltk.data.find("sentiment/vader_lexicon")
    except LookupError:
        print("Downloading NLTS lexicon...")
        nltk.download('vader_lexicon')
        print('NLTS lexicon downloaded')

def get_word_data(
        file_path: str,
        batch_size: int = 1000,
        n_process: int = 4,
        pbar: bool = False
) -> WordData:
    ensure_dependencies()

    result = WordData()

    for word in enumerate_words(file_path, batch_size=batch_size, n_process=n_process, pbar=pbar):
        result.total_word_count += 1
        if word.pos_tag not in result.pos_frequency_data:
            result.pos_frequency_data[word.pos_tag] = POSFrequencyData()
        word_pos_data = result.pos_frequency_data[word.pos_tag]
        word_pos_data.total += 1
        if word.lemma is not None:
            result.unique_words.add(word.lemma)
            word_pos_data.unique.add(word.lemma)
        if word.pos_tag == 'NOUN' and len(word.content) > len(result.longest_noun_word):
            result.longest_noun_word = word.content
        result.total_positivity += word.positivity
        result.total_negativity += word.negativity

    return result
