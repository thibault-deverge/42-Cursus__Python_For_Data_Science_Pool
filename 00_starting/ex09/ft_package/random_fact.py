import requests


def get_random_fact() -> str:
    """
    Return a random fact
    """
    url = 'https://uselessfacts.jsph.pl'
    response = requests.get(f'{url}/api/v2/facts/random?language=en')
    if response.status_code == 200:
        fact = response.json()['text']
        return fact
    else:
        return "Failed to fetch a random fact."
