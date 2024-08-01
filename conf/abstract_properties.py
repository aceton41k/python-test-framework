from abc import ABC, abstractmethod
from typing import Dict


class BasePropertyReader(ABC):
    properties: Dict = None

    def __init__(self):
        self.read_properties()

    def get_properties(self):
        return self.properties

    @abstractmethod
    def read_properties(self):
        pass
