import warnings
import numpy as np

class CameraProperties(object):
    def __init__(self, cam_fov: tuple, cam_res: tuple, name: str = 'default camera') -> None:
        self.name = name
        self.camera_fov = cam_fov # tuple of (theta_x, theta_y) in degrees
        self.camera_res = cam_res # tuple of (width, height) in pixels

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if not hasattr(self, 'name'):
            self.__name = name
        else:
            self._already_set('name')

    @property
    def camera_fov(self) -> tuple:
        return self.__camera_fov

    @camera_fov.setter
    def camera_fov(self, camera_fov: tuple):
        if not hasattr(self, 'camera_fov'):
            self.__camera_fov = camera_fov
        else:
            self._already_set('camera_fov')

    @property
    def camera_res(self) -> tuple:
        return self.__camera_res

    @camera_res.setter
    def camera_res(self, camera_res: tuple):
        if not hasattr(self, 'camera_res'):
            self.__camera_res = camera_res
        else:
            self._already_set('camera_fov')

    @property
    def focal_distance(self):
        x_d = (self.camera_res[0]/2) / (np.tan(np.deg2rad(self.camera_fov[0]/2)))
        y_d = (self.camera_res[1]/2) / (np.tan(np.deg2rad(self.camera_fov[1]/2)))
        return ((x_d + y_d) / 2)

    @staticmethod
    def _already_set(attribute: str):
        warnings.warn('property {} already set'.format(attribute), SyntaxWarning, stacklevel = 3)

