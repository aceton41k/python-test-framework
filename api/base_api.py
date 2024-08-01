from conf.abstract_properties import BasePropertyReader


class BaseApi:
    properties = None

    def __init__(self, reader: BasePropertyReader):
        self.properties = reader.get_properties()

    def get_url(self):
        pass
