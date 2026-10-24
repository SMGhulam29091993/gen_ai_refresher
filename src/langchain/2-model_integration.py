# MODEL INTEGRATION

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model #this library is used to initialize any kind of chat model, including Gemini, OpenAI, and Grok.
import logging
from pydantic import SecretStr
from langchain_groq import ChatGroq

load_dotenv()

logging.getLogger("google_genai.models").setLevel(logging.ERROR)

gemini_api_key = os.getenv("GEMINI_API_KEY")
# openai_api_key = os.getenv("OPENAI_API_KEY")
# grok_api_key = os.getenv("GROK_API_KEY")

if not gemini_api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set. Please set it in your .env file.") 

# if not openai_api_key:
#     raise RuntimeError("OPENAI_API_KEY environment variable is not set. Please set it in your .env file.")  

# if not grok_api_key:
#     raise RuntimeError("GROK_API_KEY environment variable is not set. Please set it in your .env file.")

# Initialize Gemini model
gemini_model = init_chat_model("gemini-3.5-flash", model_provider="google_genai", api_key=gemini_api_key)  

# Initialize OpenAI model
# openai_model = init_chat_model("gpt-4o-mini", model_provider="openai", api_key=openai_api_key)

# Initialize Grok model
grok_model = ChatGroq(model="openai/gpt-oss-120b") # Initialize Grok model using langchain_groq library

# openai_model_response = openai_model.invoke(
#     "Hello OpenAI! how are you doing today?"
# )

# grok_model_response = grok_model.invoke(
#     "Hello Grok! how are you doing today?"
# )


gemini_model_response = gemini_model.invoke(
    "Hello Gemini! how are you doing today?"
)

print("Gemini Model Response:", gemini_model_response.text)
# print("OpenAI Model Response:", openai_model_response.text)
# print("Grok Model Response:", grok_model_response)


