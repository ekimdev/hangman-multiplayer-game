"""
Módulo con funciones para obtener una palabra desde
distintos medios
"""
import requests


def get_word_from_internet() -> str:
    url = "https://palabras-aleatorias-public-api.herokuapp.com/random"

    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error: ", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.TooManyRedirects as errtm:
        print("Too Many Redirects Error: ", errtm)
    except requests.exceptions.RequestException as err:
        print("Oops: ", err)
    else:
        return response.json()["body"]["Word"]


def get_word_from_file(filename: str) -> str:
    pass


def get_word():
    pass
