import pytest
from src import circle


@pytest.mark.parametrize(
    ("circle_range", "perimetr"),
        [
            (8, 50.26548245743669),
            (6.6, 41.46902302738527),
        ],
    ids=["integer", "float"]
)
def test_circle_get_perimetr_positive(circle_range, perimetr):
    assert circle.Circle(circle_range).get_perimetr == perimetr


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_circle_get_area_positive(db, type_of_number):
    circle_range, area = db(type_of_figure = "circle", type_of_number = type_of_number)
    assert circle.Circle(circle_range).get_area == area


@pytest.mark.parametrize(
    ("circle_range"),
    [
        (None),
        (-1),
        ("10")
    ],
    ids=["circle_range is None", "circle_range = -1", "circle_range = string"]
)
def test_circle_negative(circle_range):
    with pytest.raises(ValueError):
        circle.Circle(circle_range)


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_circle_add_area_positive(db, type_of_number):
    circle_range, area = db(type_of_figure = "circle", type_of_number = type_of_number)
    r = circle.Circle(circle_range)
    assert r.add_area(r) == area


@pytest.mark.parametrize(
    ("area"),
    [
        (8),
        ("6.6")
    ],
    ids=["area = int", "area = string"]
)
def test_circle_add_area_negative(area):
    with pytest.raises(ValueError):
        circle.Circle(8).add_area(area)
