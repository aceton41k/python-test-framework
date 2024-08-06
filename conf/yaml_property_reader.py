import os
import pathlib
from typing import Dict

import yaml

from conf.abstract_properties import BasePropertyReader


class YamlPropertyReader(BasePropertyReader):
    properties: Dict = None

    def read_properties(self):
        path = os.path.abspath(pathlib.Path('', 'properties.yaml'))
        with open(path, 'r') as file:
            self.properties = yaml.safe_load(file)

    def get_properties(self):
        return self.properties
