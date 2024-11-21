import cohere
from config.settings import COHERE_API_KEY

class CohereService:
    def __init__(self):
        self.client = cohere.Client(COHERE_API_KEY)
    
    def rerank_responses(self, query, responses, num_responses=10):
        reranked_responses = self.client.rerank(
            model='rerank-english-v2.0',
            query=query,
            documents=responses,
            top_n=num_responses,
        )
        return reranked_responses 