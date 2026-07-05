import os 
from dotenv import load_dotenv
load_dotenv()
from google.api_core.exceptions import GoogleAPIError
from google import genai
api_key= os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key = api_key)

def ask_gemini(chat_history):
    try:
        print("Thinking...")
        response = client.models.generate_content(
            model = "gemini-2.5-flash-lite",
            contents = chat_history
        )
        chat_history.append({'role':'model','parts':[{'text': response.text}]})
        return response.text
    except GoogleAPIError as e:
        print(f"Google API Error occurred: {e}" )
        return "A Google API error occurred while generating the response."
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Something went wrong"

def make_plan(task_details):
    try:
        print("Planning your day...")
        response = client.models.generate_content(
            model = "gemini-2.5-flash-lite",
            contents = task_details
        )
        task_details.append({'role' : 'model', 'parts' : [{'text': response.text}]})
        return response.text
    except GoogleAPIError as e:
        print(f"Google API Error occurred: {e}" )
        return "A Google API error occurred while generating the response." 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "Something went wrong"