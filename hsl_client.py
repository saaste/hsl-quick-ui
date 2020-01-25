from datetime import datetime
import requests


def get_next_route(origin, destination):
    endpoint = "https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql"
    headers = {'Content-Type': 'application/graphql'}
    query = """
    {
        plan(
            fromPlace: "%s"
            toPlace: "%s"
            numItineraries: 1
            walkReluctance: 2.1
        ) {
            itineraries {
                walkDistance
                duration
                legs {
                    startTime
                    endTime
                    mode
                    duration
                    realTime
                    distance
                    transitLeg
                    from {
                        name
                        stop {
                            code
                            name
                        }
                    }
                    to {
                        name
                        stop {
                            code
                            name
                        }
                    }
                    trip {
                        tripHeadsign
                        routeShortName
                    }
                }
            }
        }
    }
    """ % (origin, destination)

    response = requests.post(endpoint, data=query, headers=headers)

    error = None
    result = {}

    if response.status_code != 200:
        raise Exception("Reittikysely epäonnistui!")
    else:
        result = response.json()

    routes = []
    itineraries = result['data']['plan']['itineraries']
    for itinerary in itineraries:
        for leg in itinerary['legs']:
            mode = leg['mode']
            if mode != 'WALK':
                start_time = datetime.fromtimestamp(int(leg['startTime']) / 1000)
                route_name = leg['trip']['routeShortName']
                stop_name = leg['from']['stop']['name']
                stop_code = leg['from']['stop']['code']
                res = "%s %s at %s from %s (%s)" % (mode, route_name, start_time, stop_name, stop_code)
                routes.append(res)
    return routes
