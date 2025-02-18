from main import MakeRequest
from queries import *
import os

def GetPlayerInformation(slug: str):

    variables = {
        "slug": slug,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, PLAYER_INFORMATION_QUERY, variables)

def GetPlayerTournaments(slug: str, page: int):

    variables = {
        "slug": slug,
        "page": page,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, PLAYER_TOURNAMENT_QUERY, variables)

def GetPlayerEvents(slug: str, page: int, videogameId):

    variables = {
        "slug": slug,
        "page": page,
        "videogameId": videogameId,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, PLAYER_EVENTS_QUERY, variables)

