import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# API Keys and URLs
COHERE_API_KEY = os.environ['COHERE_API_KEY']
WEAVIATE_API_KEY = os.environ['WEAVIATE_API_KEY']
WEAVIATE_API_URL = os.environ['WEAVIATE_API_URL'] 