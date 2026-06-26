import requests
from actions.utils.variables import insert

class HTTPRequestHandler:

    def run(self, config, context):

        method = config.get("method", "GET")
        url = insert(
            config.get("url"),
            context
        )

        payload = context

        response = requests.request(
            method=method,
            url=url,
            json=payload,
            timeout=10
        )

        context["http_response"] = {
            "status_code": response.status_code
        }

        return context