import tekore as tk

class SpotifyAuthorization:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def authorize(self):
        """Autoriza o acesso à API do Spotify e retorna um objeto para acessá-la."""
        app_token = self._get_app_token()
        return tk.Spotify(app_token)

    def _get_app_token(self):
        """Obtém um token de cliente para autenticar e autorizar as solicitações à API do Spotify."""
        app_token = tk.request_client_token(self.client_id, self.client_secret)
        return app_token