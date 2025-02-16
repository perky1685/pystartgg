import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

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
        createdAt
        endAt
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
            createdAt
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


#print(json.dumps(GetResults("kayane-cup-arc-world-tour-2024", 33945), indent=2))
#print(GetTournamentInformation("kayane-cup-arc-world-tour-2024"))
#print(GetEventResults("kayane-cup-arc-world-tour-2024", 33945))
#print(GetEventsInformation("kayane-cup-arc-world-tour-2024", [33945, 48548]))