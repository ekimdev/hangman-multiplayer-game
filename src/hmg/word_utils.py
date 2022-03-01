"""
Módulo con funciones para obtener una palabra desde
distintos medios
"""
import requests


def get_word_from_internet() -> str:
    url = "https://palabras-aleatorias-public-api.herokuapp.com/random"
    response = requests.get(url)
    return response.json()["body"]["Word"]
