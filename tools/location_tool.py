import requests

def get_coordinates(location_name):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location_name,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "TripPlannerAgent"
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    if data:
        return data[0]["lat"], data[0]["lon"]
    else:
        return None, None
