import requests

from lemur_requests import *


class LemurGraphQLClient:
    api_url: str
    headers: dict

    def __init__(self, api_url: str, headers: dict):
        self.api_url = api_url
        self.headers = headers

    def _execute(self, query: str, variables: dict) -> dict:
        payload = {
            'query': query,
            'variables': variables
        }

        r = requests.post(self.api_url, json=payload, headers=self.headers)

        if r.status_code not in [200, 201]:
            return None

        body: dict = r.json()

        # if body.get('errors'):
        #     print(body['errors'])

        return body

    def get_game(self, unique_id: int):
        return self._execute(
            query=get_game_query,
            variables={"uniqueId": unique_id}
        )

    def update_game(self, game: dict):
        return self._execute(
            query=update_game_mutation,
            variables=game
        )
