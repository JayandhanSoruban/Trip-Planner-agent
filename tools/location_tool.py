from typing import Dict

class LocationTool:
    def get_location(self, origin: str, destination: str) -> Dict[str, str]:
        """
        Returns cleaned location info.
        """
        return {
            "origin": origin.strip().title(),
            "destination": destination.strip().title()
        }
