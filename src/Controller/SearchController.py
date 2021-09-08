from src.Service.Connection.SpotifyApiConnection import SpotifyApiConnection
from src.Service.ConfigData.ConfigDataService import ConfigDataService
from src.Service.Authorization.AuthenticationService import AuthenticationService

#TODO: add Logger
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