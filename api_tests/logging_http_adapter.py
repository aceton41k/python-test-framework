import json

from requests.adapters import HTTPAdapter


class LoggingHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request_info = {}
        self.response_info = {}

    def send(self, request, **kwargs):
        self.request_info.clear()
        self.request_info['Method'] = request.method
        self.request_info['Request URL'] = request.url
        self.request_info['Request Headers'] = dict(request.headers)
        self.request_info['Request Data'] = request.body

        response = super().send(request, **kwargs)

        self.response_info.clear()
        self.response_info['Response Code'] = response.status_code
        self.response_info['Response Headers'] = dict(response.headers)
        try:
            response_body = response.json()
            formatted_response_body = json.dumps(response_body, indent=2)
        except ValueError:
            formatted_response_body = response.text
        self.response_info['Response Body'] = '\n'+formatted_response_body

        return response

    @staticmethod
    def format_info(info_dict):
        formatted_info = []
        for key, value in info_dict.items():
            if isinstance(value, dict):
                formatted_info.append(f"{key}:")
                for sub_key, sub_value in value.items():
                    formatted_info.append(f"{sub_key}: \t{sub_value}")
            else:
                formatted_info.append(f"{key}:\t{value}")
        return "\n".join(formatted_info)
