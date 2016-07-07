import requests
from ltg import settings

def google_auth(access_token):
    response = requests.get(
        settings.GOOGLE_USER_INFO_URL,
        params={'access_token': access_token}
    )

    return response.json()
