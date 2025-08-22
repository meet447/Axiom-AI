from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
UNIO_API_KEY = os.getenv('UNIO_API_KEY')