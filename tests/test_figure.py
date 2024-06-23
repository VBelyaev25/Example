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
def test_figure_area_positive(side_a, side_b, area):
    assert rectangle.Rectangle(side_a, side_b).get_area == area


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        ("3", 5),
        (3.5, "5.5"),
        (3.5, -5.5),
        (0, 5.5)
    ],
     ids=["side_a is string", "side_b is string", "side_b < 0", "side_a = 0"]
)
def test_figure_negative(side_a, side_b):
    with pytest.raises(ValueError):
        rectangle.Rectangle(side_a, side_b)


@pytest.mark.skip(reason = 'This test skip for exampe')
def test_example_for_pass():
    assert True == False


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
        (8, 5, 40),
        (0.1, 0.1, 0.010000000000000002)
    ],
     ids=["side_a 8 side_b 5 ",  "side_b 0.1 side_a = 0.1"]
)
def test_some_area(side_a, side_b, area):
    r = rectangle.Rectangle(side_a, side_b)
    assert r.get_area == area
