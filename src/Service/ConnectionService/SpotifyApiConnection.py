from .ConnectionServiceInterface import ConnectionServiceInterface
import requests

#TODO: manage token expiry time
class SpotifyApiConnection(ConnectionServiceInterface):
    def __init__(self, config: dict):
        ConnectionServiceInterface.__init__(self)
        self.config = config

    def _get_request_body(self):
        return self.config['oauth']['request_body']

    def _get_request_headers(self, data):
        auth_scheme = self.config['oauth']['auth_scheme']
        return {"Authorization": f"{auth_scheme} {data}"}

    def get_token(self, client_credentials: str):
        token = False
        if self.config:
            request = requests.post(self.config['oauth']['token_url'], data=self._get_request_body(), headers=self._get_request_headers(client_credentials))
            if request.status_code in range(200, 299):
                token = request.json()
        return token

    def get_search_request(self, token):
        request = False
        if (token):
            request = requests.get('https://api.spotify.com/v1/search?q=radiohead&type=track&limit=3', headers={"Authorization": f"Bearer {token}"})
        return request.json()