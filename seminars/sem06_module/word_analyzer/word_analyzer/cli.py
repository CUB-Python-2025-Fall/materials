import click
from .worddata import get_word_data


@click.command()
@click.argument(
    "file_path",
    type=click.Path(exists=True, dir_okay=False, readable=True),
    required=True
)
@click.option(
    "--batch-size",
    type=int,
    default=1000,
    show_default=True,
    help="Number of items per batch"
)
@click.option(
    "--n-process",
    type=int,
    default=4,
    show_default=True,
    help="Number of parallel processes"
)
@click.option(
    "--no-pbar",
    is_flag=True,
    default=False,
    help="Disable progress bar"
)
def main(file_path: str, batch_size: int, n_process: int, no_pbar: bool):
    click.echo("Start processing")
    word_data = get_word_data(
        file_path=file_path,
        batch_size=batch_size,
        n_process=n_process,
        pbar=not no_pbar
    )

    click.echo("Word Analysis Results:")
    click.echo(click.style(str(word_data), fg='green'))


if __name__ == "__main__":
    main()
