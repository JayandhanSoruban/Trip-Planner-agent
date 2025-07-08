from agents.location_agent import extract_location_name
from tools.location_tool import get_coordinates

def main():
    print("🌍 Trip Planner Agent")
    while True:
        user_input = input("🧭 Where do you want to go? ").strip()
        if user_input:
            break
        print("⚠️ Please enter a valid destination.")

    # Now user_input is guaranteed to be valid
    print(f"📍 Destination accepted: {user_input}")
    
    try:
        location_name = extract_location_name(user_input)
        print(f"📍 Destination extracted: {location_name}")

        lat, lon = get_coordinates(location_name)
        print(f"🗺️ Coordinates: Latitude: {lat}, Longitude: {lon}")

    except Exception as e:
        import traceback
        #print(location_name)
        print(f"❌ Error: {str(e)}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
