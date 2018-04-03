import math
import numpy as np


class DistanceFinder(object):
    def __init__(self, cam_props, target_props, name: str = "DistanceFinder"):
        self._target = target_props
        self._camera = cam_props
        self.name = name

    def find_distance(self, point1: tuple, point2: tuple) -> float:
        point1 = self._camera.convert_point(point1)
        point2 = self._camera.convert_point(point2)

        cam_distance = self._camera.focal_distance
        cam_res = self._camera.camera_res
        coefficient = (1, -1)
        object_displacement = self._target.target_width

        point_displacement_squared = sum(
            [(co*(p1 - p2))**2 for p1, p2, co in zip(
                point1, point2, coefficient)])
        distance_squared = (cam_distance**2 * object_displacement**2) \
            / point_displacement_squared
        object_distance = math.sqrt(distance_squared)
        return object_distance

    def find_displacement(self, point1: tuple, point2: tuple):
        z_distance = self.find_distance(point1, point2)

        point1 = self._camera.convert_point(point1)
        point2 = self._camera.convert_point(point2)

        midpoint = np.mean((point1, point2), axis=0)

        y_distance = (z_distance * midpoint[1]) / self._camera.focal_distance
        x_distance = (z_distance * midpoint[0]) / self._camera.focal_distance

        return (x_distance, y_distance, z_distance)
