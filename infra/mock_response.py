import json

from requests import HTTPError


class MockResponse:
    def __init__(self, text, status_code=200, reason='OK', content=None):
        self.text = text
        self.status_code = status_code
        self.reason = reason
        self.content = content

    def json(self):
        return json.loads(self.text)

    def raise_for_status(self):
        raise HTTPError('Mock Http Error', response=self)