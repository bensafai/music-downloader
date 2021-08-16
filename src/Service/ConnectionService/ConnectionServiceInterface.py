from abc import ABC, abstractmethod


class ConnectionServiceInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def _get_config(self):
        pass

    @abstractmethod
    def _get_client_credentials(self, client_id, client_secret):
        pass

    @abstractmethod
    def _get_request_data(self):
        pass

    @abstractmethod
    def _get_request_headers(self, client_credential):
        pass

    @abstractmethod
    def get_response(self):
        pass