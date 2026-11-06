import pytest

from ai_foundations.week00.stats import mean


def test_mean_of_simple_list() -> None:
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_of_single_value() -> None:
    assert mean([5.0]) == 5.0


def test_mean_of_empty_list_raises() -> None:
    with pytest.raises(ValueError):
        mean([])
