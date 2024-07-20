import json


class Structures:
    def structures(self):
        skills = ['web', 'html', 'js', 'css']
        data = {'id': 123, 'name': 'Peter', 'skills': skills, 'list': (1, 'LAL', 3)}
        dct = {'data': data, 'message': 'ok', 'code': 200}
        print(json.dumps(dct, indent=2))

    def __init__(self):
        pass


structures = Structures()
structures.structures()
