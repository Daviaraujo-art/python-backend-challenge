"""Tests for the AVL tree and file processing."""

import importlib.util
from pathlib import Path

import pytest

from my_structure import MyStructure


def test_duplicates_and_order():
    structure = MyStructure()
    assert [structure.add(n) for n in [5, 3, 5, -1, 3, 9]] == [
        True,
        True,
        False,
        True,
        False,
        True,
    ]
    assert structure.values() == [-1, 3, 5, 9]


@pytest.mark.parametrize("numbers", [list(range(1000)), list(range(999, -1, -1))])
def test_sorted_inputs_remain_balanced(numbers):
    structure = MyStructure()
    for number in numbers:
        assert structure.add(number)
    assert structure.values() == list(range(1000))
    assert structure._root is not None
    assert structure._root.height <= 11


def test_empty_tree():
    assert MyStructure().values() == []


def test_file_processing(tmp_path):
    spec = importlib.util.spec_from_file_location(
        "challenge_main", Path(__file__).resolve().parents[1] / "__main__.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    source, destination = tmp_path / "in.txt", tmp_path / "out.txt"
    source.write_text("4\n-2\n4\n", encoding="utf-8")
    assert module.process(source, destination) == [-2, 4]
    assert destination.read_text(encoding="utf-8") == ("4: NEW\n-2: NEW\n4: REPEATED\n")
