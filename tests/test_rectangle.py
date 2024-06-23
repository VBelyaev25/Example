import pytest
from src import rectangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
        (3, 5, 15),
        (3.5, 5.5, 19.25)
    ],
     ids=["integer", "float"]
)
def test_rectangle_area_positive(side_a, side_b, area):
    assert rectangle.Rectangle(side_a, side_b).get_area == area


@pytest.mark.parametrize(
    ("side_a", "side_b", "perimetr"),
        [
            (8, 7, 30),
            (6.5, 5.5, 24),
        ],
    ids=["integer", "float"]
)
def test_rectangle_get_perimetr_positive(side_a, side_b, perimetr):
    assert rectangle.Rectangle(side_a, side_b).get_perimetr == perimetr


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        ("3", 5),
        (3.5, bytearray(b'15')),
        (3.5, -5.5),
        (None, 5.5)
    ],
     ids=["side_a is string", "side_b is bytearray 15", "side_b < 0", "side_a = None"]
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        rectangle.Rectangle(side_a, side_b)


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_rectangle_add_area_positive(db, type_of_number):
    side_a, side_b, area = db(type_of_figure = "rectangle", type_of_number = type_of_number)
    r = rectangle.Rectangle(side_a, side_b)
    assert r.get_area == area


@pytest.mark.parametrize(
    ("area"),
    [(8), ("6.6")],
    ids=["area = int", "area = string"]
)
def test_rectangle_add_area_negative(area):
    with pytest.raises(ValueError):
        rectangle.Rectangle(5, 6).add_area(area)
