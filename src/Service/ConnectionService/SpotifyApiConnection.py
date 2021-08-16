from .ConnectionServiceInterface import ConnectionServiceInterface
import base64
import requests
import yaml
import os.path

#TODO: manage token expiry time
class SpotifyApiConnection(ConnectionServiceInterface):
    CONFIG_FILE_PATH = './config.yml'

    def __init__(self, client: str):
        ConnectionServiceInterface.__init__(self)
        self.client = client

    def _get_config(self):
        config_data = False
        file_exists = os.path.isfile(self.CONFIG_FILE_PATH)
        if file_exists:
            with open(self.CONFIG_FILE_PATH) as file:
                config_file = yaml.full_load(file)
                config_data = config_file[self.client]
        return config_data

    def _get_request_data(self, data):
        return {"grant_type": "client_credentials"}

    def _get_request_headers(self, client_credential):
        return {"Authorization": f"Basic {client_credential}"}

    def _get_client_credentials(self, client_id, client_secret):
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_response(self):
        token = False
        config = self._get_config()
        if config:
            credential = self._get_client_credentials(config['oauth_api']['client_id'], config['oauth_api']['client_secret'])
            request = requests.post(config['oauth_api']['oath_token_url'], data=self._get_request_data(), headers=self._get_request_headers(credential))
            if request.status_code in range(200, 299):
                token = request.json()
        return token