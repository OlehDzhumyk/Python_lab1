from Radial import Radial


class Ellipsoid(Radial):

    def __init__(self, first_radius: float, second_radius: float):
        super().__init__(first_radius)
        self.second_radius = second_radius

    def print(self):
        print(f"I am ellipsoid. First radius = {self.radius}, second radius = {self.second_radius}.")
