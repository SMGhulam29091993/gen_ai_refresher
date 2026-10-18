import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable is not set. Please set it in your .env file.")
