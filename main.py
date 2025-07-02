from memory.memory_manager import MemoryManager
from agents.location_agent import LocationAgent

if __name__ == "__main__":
    print("🚀 Trip Planner Agent Started")
    
    memory = MemoryManager()
    location_agent = LocationAgent(memory)

    origin = input("🌍 Where do you currently live? ")
    destination = input("✈️  Where do you want to go? ")

    location_result = location_agent.run(origin, destination)
    
    print(location_result)
    print("🧠 Current Memory State:", memory.dump())
