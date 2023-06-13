import tekore as tk

def authorize():
    """Pega as credenciais e autoriza o acesso. Retorna um objeto que nos permite acessar a API."""
    CLIENT_ID = "f6ba63651f854785af79bde32ef60c26"
    CLIENT_SECRET = "dedda806113041afa823350135d90e2d"
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)
