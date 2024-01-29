"""
This is secret client,
it develops but should not affect other gathers.
util usage for requesting the target
"""
import requests
from util.exception import RichCannotParseJSON, RichRequestNotSuccess, RichCannotRequest


class Wallex:
    def markets(self):
        try:
            response = requests.get("https://api.wallex.ir/v1/markets")
        except Exception as e:
            raise RichCannotRequest(e)

        if response.status_code != 200:
            raise RichRequestNotSuccess(f"status code: {response.status_code} || BODY: {response.text}")

        try:
            response = response.json()
        except Exception as e:
            raise RichCannotParseJSON(e)

        if not response.get("success", None):
            raise RichRequestNotSuccess(f"SUCCESS: {response.get('success', None)} | Body: {response}")

        return response.get("result", None).get("symbols", None) or None
