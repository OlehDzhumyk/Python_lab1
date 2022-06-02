from abc import ABC, abstractmethod


class SpatialFigures(ABC):
    @abstractmethod
    def print(self):
        print("I am spatial figures")
