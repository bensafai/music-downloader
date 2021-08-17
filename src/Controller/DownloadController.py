from ..Service.ConnectionService.SpotifyApiConnection import SpotifyApiConnection
from ..Service.ConnectionService.NapsterApiConnection import NapsterApiConnection
from ..Service.ConnectionService.ConfigDataService import ConfigDataService
from ..Service.ConnectionService.AuthenticationService import AuthenticationService


class DownloadController:
    def __init__(self, client_name: str):
        self.client = client_name
        #client = SpotifyApiConnection(source, 'oauth', 'client_credentials')
        #self.token = client.get_response()

        #search = SpotifyApiConnection(source, 'search', 'client_credentials')
        #self.token = search.get_response()

    def request_action(self):
        config_data = ConfigDataService(self.client)
        config =  config_data.get_config()

        auth_service = AuthenticationService(config['oauth']['client_id'], config['oauth']['client_secret'])
        client_credentials = auth_service.get_client_credentials()

        connection_service = SpotifyApiConnection(config)
        token = connection_service.get_token(client_credentials)
        search = connection_service.get_search_request(token['access_token'])
        return search