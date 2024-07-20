import json
from collections import namedtuple
from json import JSONEncoder
import requests

from api.bored_api import BoredApi
from model.activity import Activity


# Замените этот URL на адрес вашего API

class MainTests:

    def test_api_status_code(self):
        api = BoredApi()
        api.get_activity()


class ActivityEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def custom_activity_decoder(activity_dict):
    return namedtuple('X', activity_dict.keys())(*activity_dict.values())
