from ..Service.ConnectionService.SpotifyApiConnection import SpotifyApiConnection
from ..Service.ConnectionService.NapsterApiConnection import NapsterApiConnection


class DownloadController:
    def __init__(self, source: str):
        client = SpotifyApiConnection(source)
        self.token = client.get_response()

    def request_action(self):
        return self.token