"""Read integers, classify occurrences, and print unique sorted values."""

import argparse
from pathlib import Path

from my_structure import MyStructure


def process(input_path: Path, output_path: Path) -> list[int]:
    """Write a status for each input number and return unique values."""
    structure = MyStructure()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with input_path.open(encoding="utf-8") as source, output_path.open(
        "w", encoding="utf-8"
    ) as destination:
        for line_number, line in enumerate(source, start=1):
            try:
                number = int(line.strip())
            except ValueError as exc:
                raise ValueError(
                    f"Invalid integer on line {line_number}: {line.strip()!r}"
                ) from exc
            status = "NEW" if structure.add(number) else "REPEATED"
            destination.write(f"{number}: {status}\n")
    return structure.values()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Input text file")
    parser.add_argument("output", type=Path, help="Output text file")
    args = parser.parse_args()
    values = process(args.input, args.output)
    print("Unique numbers (ascending):", *values)


if __name__ == "__main__":
    main()
