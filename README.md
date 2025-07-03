✅ Project Description
"This is an LLM-driven autonomous travel planner built with LangChain and powered by HuggingFace. It receives a user query like 'Plan a 3-day trip to Rome', intelligently breaks it down into subtasks, delegates those subtasks to specialized tools (agents), and finally synthesizes a complete itinerary based on live weather, attractions, and location data."

🧠 LLM: Responsible for natural language understanding, reasoning, and orchestration of tools.

🛠️ Tools/Agents: Handle deterministic tasks like getting weather, finding coordinates, or fetching attractions.

🔁 LangChain Agent: Binds LLM and tools into a reasoning loop (ReAct), allowing dynamic task planning.

User: "Plan a 2-day trip to Rome"

      ▼

[LangChain Agent]
  🧠 LLM understands query
  🔁 Decides tasks dynamically using ReAct loop

      ▼

Calls ↓
  ├── get_location("Rome")     → lat, lon
  ├── get_weather(lat, lon)    → forecast
  └── get_activities("Rome")   → top places

      ▼

[LLM Final Response]
Generates beautiful natural itinerary using all returned tool outputs

      ▼

🧾 Output:
"Day 1: Visit the Colosseum..."
