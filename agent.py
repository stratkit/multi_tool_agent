import datetime
import os
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
import pandas as pd


# -----------------------
# Tool 1: Weather Tool
# -----------------------
def get_weather(city: str) -> dict:
    # """Returns current weather for supported cities."""
    city = city.lower()
    weather_data = {
        "new york": "sunny with a temperature of 25°C (77°F)",
        "chicago": "cloudy with a temperature of 18°C (64°F)",
        "omaha": "partly cloudy with a temperature of 22°C (71°F)",
        "san francisco": "foggy with a temperature of 17°C (63°F)"
    }

    if city in weather_data:
        return {
            "status": "success",
            "report": f"The weather in {city.title()} is {weather_data[city]}."
        }
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have weather data for {city.title()}."
        }


# -----------------------
# Tool 2: Current Time Tool
# -----------------------
def get_current_time(city: str) -> dict:
    # """Returns the current time in a specified city."""
    timezones = {
        "new york": "America/New_York",
        "chicago": "America/Chicago",
        "omaha": "America/Chicago",
        "san francisco": "America/Los_Angeles"
    }

    tz_id = timezones.get(city.lower())
    if not tz_id:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have timezone info for {city}."
        }

    now = datetime.datetime.now(ZoneInfo(tz_id))
    return {
        "status": "success",
        "report": f"The current time in {city.title()} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}."
    }


# -----------------------
# Tool 3: Project Data Search Tool
# -----------------------
def search_projects(keyword: str) -> dict:

    # Debugging to find the data folder path
    # print("DEBUG: Current working directory is:", os.getcwd())
    # print("DEBUG: __file__ location is:", __file__)

    
    # """Searches project_data.csv for rows containing the keyword."""
    try:
        # df = pd.read_csv("data/project_data.csv")
        file_path = os.path.join(os.path.dirname(__file__), "data", "project_data.csv")
        df = pd.read_csv(file_path)
        
        matches = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False).any(), axis=1)]
        if matches.empty:
            return {"status": "success", "result": f"No matches found for '{keyword}'."}
        return {"status": "success", "result": matches.to_dict(orient="records")}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}


# -----------------------
# Root Agent Definition
# -----------------------
root_agent = Agent(
    name="multi_tool_agent",
    model="gemini-2.0-flash-exp",
    description="Agent that can provide weather, current time, or internal project info.",
    instruction=(
        "You can ask me about the weather in supported cities, the current time in those cities, "
        "or to look up information from internal project data using a keyword like a client name, status, or category."
    ),
    tools=[get_weather, get_current_time, search_projects]
)
