import weaviate
from config.settings import WEAVIATE_API_KEY, WEAVIATE_API_URL, COHERE_API_KEY

class WeaviateService:
    def __init__(self):
        auth_config = weaviate.auth.AuthApiKey(api_key=WEAVIATE_API_KEY)
        self.client = weaviate.Client(
            url=WEAVIATE_API_URL,
            auth_client_secret=auth_config,
            additional_headers={
                "X-Cohere-Api-Key": COHERE_API_KEY,
            }
        ) 