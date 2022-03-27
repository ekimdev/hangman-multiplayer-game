"""
Módulo con funciones para obtener una palabra desde
distintos medios
"""
import unicodedata
import requests


def normalize_word(word: str) -> str:
    normalized_word = (
        unicodedata.normalize("NFKD", word).encode("ascii", "ignore").decode()
    )
    return normalized_word


def get_word_from_internet() -> str:
    url = "https://palabras-aleatorias-public-api.herokuapp.com/random"
    response = requests.get(url)
    word = response.json()["body"]["Word"].split()[0]
    return normalize_word(word)
