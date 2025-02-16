EVENT_RESULTS_QUERY = """query ($tourneySlug: String!, $videogameId: [ID]){
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

TOURNAMENT_INFORMATION_QUERY = """query ($tourneySlug: String!){
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

#[] for all events
#[33945, 48548] for specific events
EVENT_INFORMATION_QUERY = """query ($tourneySlug: String!, $videogameId: [ID]){
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

#NOTE: players banner will be [0] and pfp will be [1] if a banner is set
#if a banner is not set, [0] will be the pfp
PLAYER_INFORMATION_QUERY = """
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

PLAYER_TOURNAMENT_QUERY = """
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

PLAYER_EVENTS_QUERY = """
    query ($slug: String!, $page: Int!, $videogameId: [ID]) {
        user(slug: $slug) {
            id
            tournaments (query: {page: $page}) {
                nodes {
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
            }
        }
    }
    """
