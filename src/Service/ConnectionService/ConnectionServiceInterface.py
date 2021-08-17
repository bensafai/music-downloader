from abc import ABC, abstractmethod


class ConnectionServiceInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def _get_request_headers(self, data):
        pass

    @abstractmethod
    def _get_request_body(self):
        pass

    @abstractmethod
    def get_token(self, client_credentials):
        pass

    @abstractmethod
    def get_search_request(self, token):
        pass