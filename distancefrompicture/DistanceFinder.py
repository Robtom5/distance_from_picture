import math
class DistanceFinder(object):
    def __init__(self, cam_props, target_props):
        self._target_properties = target_props
        self._camera_properties = cam_props
    
    def find_distance(self, point1: tuple, point2: tuple):
        # Dim eventually is to be used to allow locating points when they are rotated by setting it to 2
        cam_distance = self._camera_properties.focal_distance
        cam_res = self._camera_properties.camera_res
        object_displacement = self._target_properties.target_width
        # Need to convert p1 to centered in image and p2 aswell
        point_displacement_squared = sum([(p1 - p2)**2 for p1, p2, res in zip(point1, point2, cam_res)])
        distance_squared = (cam_distance**2 * object_displacement**2) / point_displacement_squared
        object_distance = math.sqrt(distance_squared)
        return object_distance

