from Radial import Radial


class Generators(Radial):
    def __init__(self, radius: float, height: float):
        super().__init__(radius)
        self.height = height

    def print(self):
        print("I am radial and have generator")
