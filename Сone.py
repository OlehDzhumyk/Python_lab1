import math

from Generators import Generators


class Cone(Generators):

    def __init__(self, radius: float, height: float):
        super().__init__(radius, height)
        self.generating = math.sqrt(pow(radius, 2) + pow(height, 2))

    def print(self):
        print(f"I am cone. Height = {self.height}, radius = {self.radius}, generating = {self.generating:1.4f}.")
