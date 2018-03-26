import math
class DistanceFinder(object):
    def __init__(self, cam_props, target_props, name: str = "DistanceFinder"):
        self._target_properties = target_props
        self._camera_properties = cam_props
        self.name = name
    
    def find_distance(self, point1: tuple, point2: tuple):

        cam_distance = self._camera_properties.focal_distance
        cam_res = self._camera_properties.camera_res
        coefficient = (1,-1)
        object_displacement = self._target_properties.target_width

        point_displacement_squared = sum([(co*(p1 - p2))**2 for p1, p2, co in zip(point1, point2, coefficient)])
        distance_squared = (cam_distance**2 * object_displacement**2) / point_displacement_squared
        object_distance = math.sqrt(distance_squared)
        return object_distance

