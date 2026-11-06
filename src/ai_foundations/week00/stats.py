"""Week 0 smoke test: a tiny typed function to prove the toolchain works."""


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)
