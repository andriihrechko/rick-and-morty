import time

import requests
from django.conf import settings

from characters.models import Character

BASE_URL = settings.RICK_AND_MORTY_API_URL

def scrape_characters() -> list[CharacterItem]:
    """Scrape characters from Rick and Morty API."""
    result = []
    url = BASE_URL
    print("Starting scraping...")

    while url is not None:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Failed to fetch data")

        data = response.json()
        next_page = data.get("info", {}).get("next")
        characters = data.get("results")

        for character in characters:
            result.append(
                Character(
                    api_id=character.get("id"),
                    name=character.get("name"),
                    status=character.get("status"),
                    species=character.get("species"),
                    gender=character.get("gender"),
                    image=character.get("image"),
                )
            )
        url = next_page
        time.sleep(0.1)
    print("End scraping.")
    return result


def dump_characters_db(characters: list[Character]) -> None:
    """Dump characters to the database."""
    print("Dumping characters to database...")
    for character in characters:
        character.save()
    print("Characters dumped to database.")


def sync_characters_db() -> None:
    """Sync characters from API to database."""
    characters = scrape_characters()
    dump_characters_db(characters)
