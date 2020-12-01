"""Define the command-line interface for the linecounter program."""

from pathlib import Path


import typer


def main(
    data_file: Path = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
):
    """Display and count the lines inside of a file."""
    # TODO: Confirm that the input file is properly specified
    # TODO: Read in the input file as long as it exists
    # TODO: Count the lines of text inside of the input file
    # TODO: Display the number of lines inside of the input file
    # TODO: If required, display the contents of the file as well
    # TODO: Ensure that the program's output matches the output in the README


if __name__ == "__main__":
    typer.run(main)
