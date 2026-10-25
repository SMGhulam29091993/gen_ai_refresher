# STREAMING AND BATCH
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model #this library is used to initialize any kind of chat model, including Gemini, OpenAI, and Grok.
import logging


load_dotenv()

logging.getLogger("google_genai.models").setLevel(logging.ERROR)

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set. Please set it in your .env file.") 



# Initialize Gemini model
gemini_model = init_chat_model("gemini-3.5-flash", model_provider="google_genai", api_key=gemini_api_key)  


# Below will only provide response at once only when the model has 
# completed generating the entire response. It will not stream the 
# response as it is being generated.  
# gemini_model_response = gemini_model.invoke(
#     "Hello Gemini! how are you doing today? " \
#     "Can you write a short paragraph on AI models"
# )

# Below will stream the response as it is being generated.
for chunk in gemini_model.stream(
    "Hello Gemini! how are you doing today? " \
    "Can you write a short paragraph on AI models"
):
    print(chunk.text, end="", flush=True)

# print("Gemini Model Response:", gemini_model_response.text)

# BATCH
# It is collection of independant requests to a model that can significantly
# improve the performance and reduce the costs, as the processing 
# can be done parallel:  

response = gemini_model.batch([
    "Hello Gemini! how are you doing today? " \
    "Can you write a short paragraph on AI models",
    "Why do parrot can talk? Can you explain it in a short paragraph?",
    "What is the difference between AI and ML? Can you explain it in "\
    "a short paragraph?"
], config={"max_concurrency":5} #Limits to 5 parallel calls to the model 
)

for res in response:
    print(res.text, end="\n\n", flush=True)