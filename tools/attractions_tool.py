import requests
import os
from dotenv import load_dotenv

load_dotenv()

GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")  # Make sure your .env has this key
GEOAPIFY_API_URL = "https://api.geoapify.com/v2/places"

def get_attractions(location: str, radius: int = 5000, limit: int = 10):
    try:
        lat, lon = map(float, location.strip().split(","))
    except Exception:
        return "❌ Invalid location format. Please use 'lat, lon'."

    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "geosearch",
        "gsradius": radius,
        "gscoord": f"{lat}|{lon}",
        "gslimit": limit,
        "format": "json"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        places = data.get("query", {}).get("geosearch", [])

        if not places:
            return "❌ No nearby Wikipedia-listed places found."

        results = [f"📍 {place['title']} — {place['dist']} meters away\n🔗 https://en.wikipedia.org/?curid={place['pageid']}"
                   for place in places]

        return "Nearby Attractions:\n" + "\n\n".join(results)

    except requests.exceptions.RequestException as e:
        return f"⚠️ Request failed: {e}"
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"
