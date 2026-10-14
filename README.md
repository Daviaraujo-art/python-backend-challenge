# Python Backend Challenge

A Python 3.12 solution for detecting repeated integers without a linear membership scan.

## Data structure

`MyStructure` in `my_structure.py` implements an AVL self-balancing binary search tree. Each insertion compares the incoming number with the current node and follows only one branch. Rotations keep tree height logarithmic, guaranteeing **O(log n)** lookup/insertion in the worst case, with **O(n)** space for n distinct values. In-order traversal prints unique numbers in ascending order. No Python `set`, `dict`, or list membership check is used for duplicate detection.

## Run

```bash
python __main__.py input/numbers_01.txt output/numbers_01.txt
```

Each output line is `number: NEW` or `number: REPEATED` in input order. The program prints the unique values in ascending order to stdout. Blank or noninteger lines raise a descriptive error.

## Quality checks

```bash
pip install -r requirements-dev.txt
black --check .
flake8 .
python -m pytest -q
```

## GitHub Actions

- **Run challenge:** processes three sample input files and uploads `challenge-output-files` as a downloadable artifact.
- **Code quality:** runs Black, Flake8 and pytest on pushes and pull requests.

For a private repository, grant collaborator access to [RianKoja](https://github.com/RianKoja). For a public repository, the code is accessible without collaborator access, though an explicit invitation can still be sent.
