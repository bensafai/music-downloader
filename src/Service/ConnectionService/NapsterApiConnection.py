from .ConnectionServiceInterface import ConnectionServiceInterface


class NapsterApiConnection(ConnectionServiceInterface):
    def __init__(self):
        pass

    def get_config(self):
        return 'Napster configing'

    def get_connection(self):
        return 'Napster connecting'
