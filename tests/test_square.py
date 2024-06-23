import pytest
from src import square


@pytest.mark.parametrize(
    ("side_a",  "area"),
    [
        (5, 25),
        (5.5, 30.25)
    ],
     ids=["integer", "float"]
)
def test_square_area_positive(side_a, area):
    assert square.Square(side_a).get_area == area


@pytest.mark.parametrize(
    ("side_a",  "perimetr"),
    [
        (5, 20),
        (5.5, 22)
    ],
     ids=["integer", "float"]
)
def test_square_perimetr_positive(side_a, perimetr):
    assert square.Square(side_a).get_perimetr == perimetr


@pytest.mark.parametrize(
    ("side_a"),
    [
        ("3"),
        ({"side_a":10}),
        (-5.5),
        (None)
    ],
     ids=["side_a is string", "side_a is dict", "side_a < 0", "side_a = None"]
)
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        square.Square(side_a)


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_square_add_area_positive(db, type_of_number):
    side_a, area = db(type_of_figure = "square", type_of_number = type_of_number)
    r = square.Square(side_a)
    assert r.add_area(r) == area

@pytest.mark.parametrize(
    ("side_a"),
    [
        ("3"),
        ({"side_a":10}),
        (5.5),
        (None)
    ],
     ids=["side_a is string", "side_a is dict", "side_a is integer", "side_a = None"]
)
def test_square_add_area_negative(side_a):
    with pytest.raises(ValueError):
        square.Square(side_a).add_area(side_a)
