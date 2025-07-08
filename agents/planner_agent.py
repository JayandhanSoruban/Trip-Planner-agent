from langchain_groq import ChatGroq
import os
from langchain.agents import initialize_agent, Tool, AgentType
from tools.location_tool import get_coordinates
from tools.weather_tool import get_weather
from tools.attractions_tool import get_attractions
from dotenv import load_dotenv
import time
from langchain.tools import StructuredTool


# Load Groq API Key 
os.environ["GROQ_API_KEY"] = "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"  

# 🧠 Define the Groq LLM brain
llm = ChatGroq(
    temperature=0,
    model_name="llama3-8b-8192",  # Groq’s LLaMA3 model
)

# 🛠️ Define tools for the agent to use
tools = [
    Tool(name="LocationTool", func=get_coordinates, description="Get lat/lon of a city"),
    Tool(name="WeatherTool", func=get_weather, description="Get weather forecast from lat/lon"),
    Tool(name="AttractionsTool", func=get_attractions, description="Get tourist attractions near a location. Input format: 'lat, lon' as a string.")
]


# 🧠💡 Combine brain + tools into agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # or AgentType.OPENAI_FUNCTIONS
    verbose=True
)

# 🚀 Function to receive input and run
def run_planner(user_input: str) -> str:
    for attempt in range(3):
        try:
            return agent.run(user_input)
        except Exception as e:
            print(f"Error occurred: {e}. Retrying in 5 seconds...")
            time.sleep(5)
    return "❌ Failed after multiple attempts."
