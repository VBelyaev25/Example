import figure


class Rectangle(figure.Figure):

    def __init__(self, side_a, side_b):
        if not isinstance(side_a, int) or side_a <= 0:
            if not isinstance(side_a, float) or side_a <= 0:
                raise ValueError(f"Sindes rectangle A cant`t be less than 0 or be {type(side_a)} need class int")
        if not isinstance(side_b, int) or side_b <= 0:
            if not isinstance(side_b, float) or side_b <= 0:
                raise ValueError(f"Sindes rectangle B cant`t be less than 0 or be {type(side_b)} need class int")
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimetr(self):
        return (self.side_a + self.side_b) * 2
