import os
import requests
from dotenv import load_dotenv
from queries import *
import json

load_dotenv()

def MakeRequest(API_KEY, EVENT_QUERY, variables):
    headers = {
            'Authorization': 'Bearer ' + API_KEY,
            'Content-Type': 'application/json'
    }

    response = requests.post(
        "https://api.smash.gg/gql/alpha",
        headers=headers,
        json={'query': EVENT_QUERY, 'variables': variables}
    )

    return response.json()

def GetEventResults(tourneySlug: str, videogameId: int):

    variables = {
        "tourneySlug": tourneySlug,
        "videogameId": videogameId
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, EVENT_RESULTS_QUERY, variables)

def GetTournamentResults(tourneySlug: str):
    EVENT_QUERY = """query ($tourneySlug: String!){
    tournament(slug: $tourneySlug){
        events{
            name
            videogame {
                id
                displayName
            }
            entrants (query: {page: 1}) {
                nodes {
                    participants{
                        player {
                            id
                            prefix
                            gamerTag
                        }
                    }
                    seeds {
                        seedNum
                    }
                    standing {
                        placement
                    }
                }
            }
        }
    }
    }"""

    variables = {
        "tourneySlug": tourneySlug,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, EVENT_QUERY, variables)

def GetTournamentInformation(tourneySlug: str):

    variables = {
        "tourneySlug": tourneySlug,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, TOURNAMENT_INFORMATION_QUERY, variables)

def GetEventsInformation(tourneySlug: str, videogameId):

    variables = {
        "tourneySlug": tourneySlug,
        "videogameId": videogameId,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, EVENT_INFORMATION_QUERY, variables)

def GetPlayerInformation(slug: str):

    variables = {
        "slug": slug,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, PLAYER_INFORMATION_QUERY, variables)

def GetPlayerTournaments(slug: str, page: int, videogameId):

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


#print(json.dumps(GetResults("kayane-cup-arc-world-tour-2024", 33945), indent=2))
#print(GetTournamentInformation("kayane-cup-arc-world-tour-2024"))
#print(GetEventResults("kayane-cup-arc-world-tour-2024", 33945))
#print(GetEventsInformation("kayane-cup-arc-world-tour-2024", [33945, 48548]))
#print(GetPlayerInformation("c1aeaece"))
#print(GetPlayerEvents("c1aeaece", 1, [33945]))
#print(GetPlayerTournaments("c1aeaece", 2))
