import os
import requests
import json
from dotenv import load_dotenv

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
    EVENT_QUERY = """query ($tourneySlug: String!, $videogameId: [ID]){
    tournament(slug: $tourneySlug){
        events(filter: {videogameId: $videogameId}){
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
                        user{
                            id
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
        "videogameId": videogameId  # Added videogameId here
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, EVENT_QUERY, variables)

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
    EVENT_QUERY = """query ($tourneySlug: String!){
    tournament(slug: $tourneySlug){
        id
        city
        countryCode
        startAt
        hasOfflineEvents
        name
        numAttendees
        timezone
        venueName
        events{
            id
            name
            numEntrants
            startAt
            videogame {
                id
                displayName
            }
        }
    }
    }"""

    variables = {
        "tourneySlug": tourneySlug,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, EVENT_QUERY, variables)

def GetEventsInformation(tourneySlug: str, videogameId):
    #[] for all events
    #[33945, 48548] for specific events
    EVENT_QUERY = """query ($tourneySlug: String!, $videogameId: [ID]){
    tournament(slug: $tourneySlug){
        events(filter: {videogameId: $videogameId}) {
            id
            name
            numEntrants
            startAt
            videogame {
                id
                displayName
            }
        }
    }
    }"""

    variables = {
        "tourneySlug": tourneySlug,
        "videogameId": videogameId,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, EVENT_QUERY, variables)


def GetPlayerInformation(slug: str):
    #NOTE: players banner will be [0] and pfp will be [1] if a banner is set
    #if a banner is not set, [0] will be the pfp
    PLAYERS_QUERY = """
        query ($slug: String!) {
            user(slug: $slug) {
                id
                bio
                birthday
                genderPronoun
                images{
                    url
                }
                player {
                    id
                    prefix
                    gamerTag
                }
                name
                location {
                    country
                    state
                    city
                }
            }
        }
        """

    variables = {
        "slug": slug,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, PLAYERS_QUERY, variables)

def GetPlayerTournaments(slug: str, page: int, videogameId):
    PLAYERS_QUERY = """
        query ($slug: String!, $page: Int!) {
            user(slug: $slug) {
                id
                tournaments (query: {page: $page}) {
                    nodes {
                        id
                        slug
                        city
                        countryCode
                        startAt
                        hasOfflineEvents
                        name
                        numAttendees
                    }
                }
            }
        }
        """

    variables = {
        "slug": slug,
        "page": page,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, PLAYERS_QUERY, variables)


def GetPlayerEvents(slug: str, page: int, videogameId):
    PLAYERS_QUERY = """
        query ($slug: String!, $page: Int!) {
            user(slug: $slug) {
                id
                tournaments (query: {page: $page}) {
                    nodes {
                        events{
                            id
                            name
                            numEntrants
                            startAt
                            videogame {
                                id
                                displayName
                            }
                        }
                    }
                }
            }
        }
        """

    variables = {
        "slug": slug,
        "page": page,
    }

    API_KEY = os.getenv("API_KEY")
    return MakeRequest(API_KEY, PLAYERS_QUERY, variables)


#print(json.dumps(GetResults("kayane-cup-arc-world-tour-2024", 33945), indent=2))
#print(GetTournamentInformation("kayane-cup-arc-world-tour-2024"))
#print(GetEventResults("kayane-cup-arc-world-tour-2024", 33945))
#print(GetEventsInformation("kayane-cup-arc-world-tour-2024", [33945, 48548]))
#print(GetPlayerInformation("c1aeaece"))
#print(GetPlayerEvents("c1aeaece", 1, []))
#print(GetPlayerTournaments("c1aeaece", 2))