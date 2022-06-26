from Cube import Cube
from Ellipsoid import Ellipsoid
from Parallelepiped import Parallelepiped
from Sphere import Sphere
from Сone import Cone
from Сylinder import Cylinder

if __name__ == '__main__':
    figure_list = [Cube(1), Parallelepiped(1, 2, 3), Sphere(1), Ellipsoid(1, 2), Cone(1, 2), Cylinder(1, 2)]

    for figure in figure_list:
        figure.print()
