import requests

def check_headers(target):
    try:
        response = requests.get(target)
        return dict(response.headers)
    except requests.exceptions.RequestException:
        return {'error': 'Failed to fetch headers'}
