import figure


class Square(figure.Figure):

    def __init__(self, side_a):
        if not isinstance(side_a, int) or side_a <= 0:
            if not isinstance(side_a, float) or side_a <= 0:
                raise ValueError(f"Sindes square A cant`t be less than 0 or be {type(side_a)} need class int")
        super().__init__()
        self.side_a = side_a

    @property
    def get_area(self):
        return self.side_a ** 2

    @property
    def get_perimetr(self):
        return self.side_a * 4