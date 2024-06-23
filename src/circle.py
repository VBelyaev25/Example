import figure


class Circle(figure.Figure):

    def __init__(self, circle_range):
        if not isinstance(circle_range, int) or circle_range <= 0:
            if not isinstance(circle_range, float) or circle_range <= 0:
                raise ValueError(f"Circle range cant`t be less than 0 or be {type(circle_range)} need class int")
        super().__init__()
        import math
        self.circle_range = circle_range
        self.pi = math.pi

    @property
    def get_area(self):
        return self.pi * self.circle_range ** 2

    @property
    def get_perimetr(self):
        return 2 * self.pi * self.circle_range