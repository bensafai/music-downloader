import base64


class AuthenticationService():
    def __init__(self):
        self.client_id = ''
        self.client_secret = ''

    def get_client_credentials(self) -> str:
        """
        Makes a base64 client credentials
        :return: str
        """
        client_creds = f"{self.client_id}:{self.client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()