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


def valid_word(word: str) -> str:
    valid_word = "".join(filter(str.isalnum, word))
    return normalize_word(valid_word.lower())


def get_word_from_alternative_api() -> str:
    alternative_url = "https://random-word-api.herokuapp.com/word/?lang=es"
    while True:
        response = requests.get(alternative_url)
        word = response.json()[0].split()[0]
        final_word = valid_word(word)
        if len(final_word) > 3:
            return final_word


def get_word_from_internet() -> str:
    url = "https://palabras-aleatorias-public-api.herokuapp.com/random"

    response = requests.get(url)
    if response.status_code == 503:
        return valid_word(get_word_from_alternative_api())

    word = response.json()["body"]["Word"].split()[0]
    return valid_word(word)
