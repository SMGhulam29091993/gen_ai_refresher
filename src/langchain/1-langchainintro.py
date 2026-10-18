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

config = CreateAgent(
    model="gemini-3.8-flash",
    tools=[],
    system_prompt="You are a helpful assistant that can answer questions and provide information."
)

llm = ChatGoogleGenerativeAI(model=config.model)

agent = create_agent(
    model=llm,
    tools=config.tools,
    system_prompt= config.system_prompt
)

result = agent.invoke({"messages" : [{"role": "user", "content": "What is the capital of France?"}]})
print(result["messages"][-1].text)

