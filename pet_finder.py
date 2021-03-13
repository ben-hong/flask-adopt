import requests

CLIENT_KEY = 'kbpE47uin0RxJ0OIR8o8H8XH9BUpESY5GV5eSizsjss8J8KV2e'
SECRET_KEY = 'wPNujcxDCgkJTUQNaupwSNBOMrEvX1GI3ELbKXYh'


def token():
    resp = requests.post('https://api.petfinder.com/v2/oauth2/token', data = {
        'grant_type':'client_credentials',
        'client_id': CLIENT_KEY,
        'client_secret': SECRET_KEY
    })
    token = resp.json()
    access_token = token['access_token']
    return access_token

def animal_data():
    resp = requests.get('https://api.petfinder.com/v2/animals', headers={
        "Authorization": f"Bearer {token()}"
    })

    data = resp.json()
    return data