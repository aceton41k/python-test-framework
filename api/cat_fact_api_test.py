import requests


from api.base_api import BaseApi
from conf.abstract_properties import BasePropertyReader
from model.cat_fact import CatFact


class CatFactApi(BaseApi):
    def __init__(self, session: requests.Session, reader: BasePropertyReader):
        super().__init__(reader)
        self.session = session

    def get_url(self) -> str:
        return self.properties["api"]["cat"]["url"]

    def get_facts(self) -> list[CatFact]:
        response = self.session.get(self.get_url() + '/facts/')
        response.raise_for_status()
        assert response.status_code == 200
        return [CatFact(**item) for item in response.json()]
