import pytest
from src import triangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area"),
    [
        (5, 6, 6, 115.90506621800446),
        (5.5, 6.5, 6.5, 149.81694152130083)
    ],
     ids=["integer", "float"]
)
def test_triangle_area_positive(side_a, side_b, side_c, area):
    assert triangle.Triangle(side_a, side_b, side_c).get_area == area


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "perimetr"),
    [
        (5, 6, 7, 18),
        (5.5, 6.6, 7.7, 19.8)
    ],
     ids=["integer", "float"]
)
def test_triangle_perimetr_positive(side_a, side_b, side_c, perimetr):
    assert triangle.Triangle(side_a, side_b, side_c).get_perimetr == perimetr


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        ("3", 5 , 5),
        (3, {"side_a":10}, 6),
        (8, 6 , None)
    ],
     ids=["side_a is string", "side_b is dict", "side_c = None"]
)
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        triangle.Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_triangle_add_area_positive(db, type_of_number):
    side_a, side_b, side_c, area = db(type_of_figure = "triangle", type_of_number = type_of_number)
    r = triangle.Triangle(side_a, side_b, side_c)
    assert r.add_area(r) == area


@pytest.mark.parametrize(
    ("area"),
    [
        ("3"),
        ({"side_a":10}),
        (5.5),
        (None)
    ],
     ids=["area is string", "area is dict", "area is integer", "area = None"]
)
def test_triangle_add_area_negative(area):
    with pytest.raises(ValueError):
        triangle.Triangle(4, 5, 6).add_area(area)
