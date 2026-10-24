import logging
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from type import CreateAgent
load_dotenv()
logging.getLogger("google_genai.models").setLevel(logging.ERROR)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set. Please set it in your .env file.")

def get_weather(city: str)->str:
    '''Return the current weather for a given city.'''
    return f"The current weather in {city} is sunny with a temperature of 25°C."

def get_capital(country: str)->str:
    '''Return the capital city of a given country.'''
    capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United Kingdom": "London"
    }
    return capitals.get(country, f"Sorry, I don't know the capital of {country}.")

config = CreateAgent(
    model="gemini-3.7-flash",
    tools=[get_weather, get_capital],
    system_prompt="""
    - You are a helpful assistant. 
    - Answer only using the results of your tools.
    - If a tool says it doesn't know, tell the user you don't know. 
    - Do not use your own knowledge.
    """
)

llm = ChatGoogleGenerativeAI(model=config.model)

agent = create_agent(
    model=llm,
    tools=config.tools,
    system_prompt= config.system_prompt
)

result = agent.invoke({"messages" : [{"role": "user", "content": "What is the capital of India?"}]})
print(result["messages"][-1].text)

result = agent.invoke({"messages" : [{"role": "user", "content": "What is the weather in New York?"}]})
print(result["messages"][-1].text)

