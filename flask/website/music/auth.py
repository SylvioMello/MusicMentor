import tekore as tk

def authorize():
    """Pega as credenciais e autoriza o acesso. Retorna um objeto que nos permite acessar a API."""
    CLIENT_ID = ""
    CLIENT_SECRET = ""
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)
