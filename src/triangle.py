import figure

class Triangle(figure.Figure):

    def __init__(self, side_a, side_b, side_c):
        if not isinstance(side_a, int) or side_a <=0:
            if not isinstance(side_a, float) or side_a <= 0:
                raise ValueError(f"Sindes triangle A cant`t be less than 0 or be {type(side_a)} need class int")
        if not isinstance(side_b, int) or side_b <= 0:
            if not isinstance(side_b, float) or side_b <= 0:
                raise ValueError(f"Sindes triangle B cant`t be less than 0 or be {type(side_b)} need class int")
        if not isinstance(side_c, int) or side_c <= 0:
            if not isinstance(side_c, float) or side_c <= 0:
                raise ValueError(f"Sindes triangle C cant`t be less than 0 or be {type(side_c)} need class int")
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c


    @property
    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c


    @property
    def get_area(self):
        p = self.get_perimetr / 2
        return (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)) ** 0.5