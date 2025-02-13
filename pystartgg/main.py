import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def MakeRequest(tourneySlug: str):
    API_KEY = os.getenv("API_KEY")
    EVENT_QUERY = """query ($tourneySlug: String!){
    tournament(slug: $tourneySlug){
        id
        countryCode
        events(filter: {videogameId: "33945"}){
            id
            name
            numEntrants
            startAt
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
        "videogameId": "33945"
    }

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
    API_KEY = os.getenv("API_KEY")
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

def GetTournamentResults(tourneySlug: str):
    API_KEY = os.getenv("API_KEY")
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

def GetTournamentInformation(tourneySlug: str):
    API_KEY = os.getenv("API_KEY")
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
        events(filter: {videogameId: "33945"}){
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