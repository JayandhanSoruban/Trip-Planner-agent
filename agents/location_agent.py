from tools.location_tool import LocationTool
from memory.memory_manager import MemoryManager

class LocationAgent:
    def __init__(self, memory: MemoryManager):
        self.tool = LocationTool()
        self.memory = memory

    def run(self, origin: str, destination: str):
        locations = self.tool.get_location(origin, destination)
        self.memory.save("origin", locations["origin"])
        self.memory.save("destination", locations["destination"])
        return f"📍 Location set: From {locations['origin']} to {locations['destination']}"
