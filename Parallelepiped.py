from Cube import Cube


class Parallelepiped(Cube):

    def __init__(self, width: float, height: float, length: float):
        super().__init__(width)
        self.height = height
        self.length = length

    def print(self):
        print(f"I am parallelepiped. Width = {self.width}, height = {self.height}, length = {self.length}.")
