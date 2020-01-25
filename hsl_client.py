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
            numItineraries: 2
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

    if response.status_code != 200:
        raise Exception("Reittikysely epäonnistui!")
    else:
        result = response.json()

    routes = []
    itineraries = result['data']['plan']['itineraries']
    for itinerary in itineraries:
        steps = []
        walking_distance = int(itinerary['walkDistance'])
        duration = itinerary['duration']
        for leg in itinerary['legs']:
            mode = leg['mode']
            if mode != 'WALK':
                start_time = datetime.fromtimestamp(int(leg['startTime']) / 1000).strftime("%H:%M")
                route_name = leg['trip']['routeShortName']
                stop_name = leg['from']['stop']['name']
                stop_code = leg['from']['stop']['code']
                icon = mode_to_icon(mode)
                steps.append({
                    "mode": mode,
                    "start_time": start_time,
                    "route_name": route_name,
                    "stop_name": stop_name,
                    "stop_code": stop_code,
                    "icon": icon
                })
        routes.append({
            "walking_distance": walking_distance,
            "duration": round(duration / 60),
            "steps": steps
        })
    return routes


def mode_to_icon(mode):
    switcher = {
        "BUS": "directions_bus",
        "RAIL": "directions_railway",
        "SUBWAY": "subway",
        "TRAM": "tram"
    }
    return switcher.get(mode.upper(), "error")
