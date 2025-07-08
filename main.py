from agents.planner_agent import run_planner

if __name__ == "__main__":
    user_input = input("Where do you want to go? (e.g., 'Plan a 3-day trip to Rome'):\n")
    response = run_planner(user_input)
    print("\n🗺️ Trip Plan:\n")
    print(response)

