import pytest
from solution import sort


@pytest.mark.parametrize(
    "w,h,l,m,expected",
    [
        # STANDARD — neither bulky nor heavy
        (10, 10, 10, 1, "STANDARD"),
        # Just under thresholds (not bulky by volume or dimension, not heavy)
        (149, 149, 45, 19.9, "STANDARD"),

        # SPECIAL — bulky (by volume)
        (100, 100, 100, 1, "SPECIAL"),
        # SPECIAL — bulky (by dimension)
        (150, 10, 10, 1, "SPECIAL"),
        (10, 150, 10, 1, "SPECIAL"),
        (10, 10, 150, 1, "SPECIAL"),

        # SPECIAL — heavy only
        (10, 10, 10, 20, "SPECIAL"),
        (50, 60, 70, 25, "SPECIAL"),

        # REJECTED — both heavy and bulky
        (150, 10, 10, 20, "REJECTED"),
        (100, 100, 100, 20, "REJECTED"),

        # More boundaries
        (149, 149, 45, 20, "SPECIAL"),
        (150, 1, 1, 19.99, "SPECIAL"),
    ],
)
def test_sort_happy_path(w, h, l, m, expected):
    assert sort(w, h, l, m) == expected


def test_sort_dimension_order_irrelevant():
    """Changing the order of dimensions shouldn't change the result."""
    dims = (150, 10, 10)
    mass = 19
    expected = "SPECIAL"
    perms = [
        (dims[0], dims[1], dims[2]),
        (dims[0], dims[2], dims[1]),
        (dims[1], dims[0], dims[2]),
        (dims[1], dims[2], dims[0]),
        (dims[2], dims[0], dims[1]),
        (dims[2], dims[1], dims[0]),
    ]
    for w, h, l in perms:
        assert sort(w, h, l, mass) == expected


@pytest.mark.parametrize(
    "w,h,l,m",
    [
        # Extra sanity: near-threshold floats shouldn’t accidentally flip
        (100, 100, 99.9999, 19.9999),
        (149.9999, 149.9999, 40.0, 19.9999),
    ],
)
def test_sort_near_thresholds_not_bulky_or_heavy(w, h, l, m):
    assert sort(w, h, l, m) == "STANDARD"



@pytest.mark.parametrize(
    "w,h,l,m",
    [
        (-1, 10, 10, 1),   # negative width
        (10, -5, 10, 1),   # negative height
        (10, 10, -2, 1),   # negative length
        (10, 10, 10, -1),  # negative mass
        (0, 10, 10, 1),    # zero width
        (10, 0, 10, 1),    # zero height
        (10, 10, 0, 1),    # zero length
        (10, 10, 10, 0),   # zero mass
    ]
)
def test_sort_invalid_negative_or_zero(w, h, l, m):
    with pytest.raises(ValueError):
        sort(w, h, l, m)


@pytest.mark.parametrize(
    "w,h,l,m",
    [
        ("a", 10, 10, 1),        # non-numeric width
        (10, "b", 10, 1),        # non-numeric height
        (10, 10, "c", 1),        # non-numeric length
        (10, 10, 10, "mass"),    # non-numeric mass
    ]
)
def test_sort_invalid_non_numeric(w, h, l, m):
    with pytest.raises(TypeError):
        sort(w, h, l, m)