from dataclasses import dataclass

@dataclass
class Author:
    id: str
    name: str

    def rename(self, new_name: str):
        if not new_name:
            raise ValueError("Author name cannot be empty")
        self.name = new_name