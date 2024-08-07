import allure

from api.cat_fact_api_test import CatFactApi
from conf.yaml_property_reader import YamlPropertyReader


@allure.title("Cat Fact API")
def test_cat_fact_api(http_adapter):
    api = CatFactApi(http_adapter, YamlPropertyReader())
    fact_list = api.get_facts()
    assert len(fact_list) == 5
