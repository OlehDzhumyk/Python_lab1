from Spatial_figures import SpatialFigures


class Cube(SpatialFigures):

    def __init__(self, width: float):
        self.width = width

    def print(self):
        print(f"I am cube. Rib = {self.width}.")
