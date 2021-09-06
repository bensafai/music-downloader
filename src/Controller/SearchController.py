from src.Service.ConnectionService.SpotifyApiConnection import SpotifyApiConnection
from src.Service.ConfigService.ConfigDataService import ConfigDataService
from src.Service.AuthenticationService.AuthenticationService import AuthenticationService


class SearchController(ConfigDataService, AuthenticationService, SpotifyApiConnection):
    def __init__(self, client_name):
        super(SearchController, self).__init__()
        self.client_name = client_name
        self.config = self.get_config()
        self.client_id = self.config['oauth']['client_id']
        self.client_secret = self.config['oauth']['client_secret']

    def request_action(self):
        client_credentials = self.get_client_credentials()
        token = self.get_access_token(client_credentials)
        return self.get_search_request(token)