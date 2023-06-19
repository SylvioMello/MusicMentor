import tekore as tk

def authorize():
    """Pega as credenciais e autoriza o acesso. Retorna um objeto que nos permite acessar a API."""
    CLIENT_ID = "ec851854db1c4433a4bb215d215893ed"
    CLIENT_SECRET = "709825c655ee4c39b0dd31d17a670217"
    app_token = tk.request_client_token(CLIENT_ID, CLIENT_SECRET)
    return tk.Spotify(app_token)
