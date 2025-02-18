from main import MakeRequest
from queries import *
import os

def GetTop8(tourneySlug: str):
    EVENT_QUERY = """query ($tourneySlug: String!){
    tournament(slug: $tourneySlug){
        events{
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

results = GetTop8("set-reset-guilty-gear-strive-24")

for event in results["data"]["tournament"]["events"]:
    for entrant in event["entrants"]["nodes"]:

        for player in entrant["participants"]:
            if player["player"]["prefix"]:
                print(f"{player["player"]["prefix"]} | {player["player"]["gamerTag"]}")
            else:
                print(f"{player["player"]["gamerTag"]}")

        for seed in entrant["seeds"]:
            print(f"seed: {seed["seedNum"]}")
        
        print(f"placement: {entrant["standing"]["placement"]}")
        
