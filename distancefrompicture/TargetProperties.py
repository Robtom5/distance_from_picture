import warnings

class TargetProperties(object):
    def __init__(self, name: str, target_width: float) -> None:
        self.name = name
        self.target_width = target_width

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
    def target_width(self) -> float:
        return self.__target_width

    @target_width.setter
    def target_width(self, target_width: float) -> None:
        if not hasattr(self, 'target_width'):
            self.__target_width = target_width
        else:
            self._already_set('target_width')

    @staticmethod
    def _already_set(attribute: str):
        warnings.warn('property {} already set'.format(attribute), SyntaxWarning, stacklevel = 3)

