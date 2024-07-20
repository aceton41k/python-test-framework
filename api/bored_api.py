import json

import requests

from model.activity import Activity


class BoredApi:

    activity_response: Activity

    def __init__(self):
        pass

    def get_activity(self):
        response = requests.get(URL + '/api/activity')
        print(f'\n'+json.dumps(response.json(), indent=2))
        assert response.status_code == 200
        self.activity_response = Activity(**response.json())
        return self


URL = "https://www.boredapi.com"
