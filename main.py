from services.cohere_service import CohereService
from services.weaviate_service import WeaviateService
from utils.search import SearchUtils
from utils.display import DisplayUtils
from utils.schema_setup import create_schema

class ReRankApp:
    def __init__(self):
        # Initialize services
        self.cohere_service = CohereService()
        self.weaviate_service = WeaviateService()
        self.search_utils = SearchUtils()
        self.display_utils = DisplayUtils()
        
        # Set up schema and sample data
        print("Setting up schema...")
        create_schema(self.weaviate_service.client)
        self.add_sample_data()

    def add_sample_data(self):
        """Add sample articles if none exist"""
        try:
            result = self.weaviate_service.client.query.get(
                "Article", ["title"]
            ).with_limit(1).do()
            
            if result.get("data", {}).get("Get", {}).get("Article"):
                print("Sample data already exists")
                return
                
            sample_articles = [
                {
                    "title": "Ottawa",
                    "text": "Ottawa is the capital city of Canada. Located in Ontario, it stands on the south bank of the Ottawa River.",
                    "url": "https://www.britannica.com/place/Ottawa",
                    "views": 1000,
                    "lang": "en"
                },
                {
                    "title": "Robert Wadlow",
                    "text": "Robert Pershing Wadlow was the tallest person in recorded history. He reached a height of 8 ft 11.1 in (2.72 m).",
                    "url": "https://en.wikipedia.org/wiki/List_of_tallest_people",
                    "views": 500,
                    "lang": "en"
                }
            ]
            
            for article in sample_articles:
                self.weaviate_service.client.data_object.create(
                    data_object=article,
                    class_name="Article"
                )
            print("Sample data added successfully")
            
        except Exception as e:
            print(f"Error adding sample data: {e}")

    def demonstrate_dense_retrieval(self):
        """Step 2: Demonstrate Dense Retrieval"""
        query = "What is the capital of Canada?"
        results = self.search_utils.dense_retrieval(query, self.weaviate_service.client)
        
        # Original version (for debugging)
        self.display_utils.print_section_header("Dense Retrieval Results (Debug)")
        for i, result in enumerate(results):
            print(f"Debug #{i+1}:")
            print(result)
            self.display_utils.print_divider("-", 30)
            
        # User friendly version
        self.display_utils.print_section_header("Dense Retrieval Results")
        print(f"🔍 Query: '{query}'\n")
        self.display_utils.print_result(results)

    def demonstrate_keyword_search_with_rerank(self):
        """Step 3: Demonstrate Keyword Search with ReRank"""
        query = "What is the capital of Canada?"
        
        # First with 3 results
        results_3 = self.search_utils.keyword_search(
            query, 
            self.weaviate_service.client,
            num_results=3
        )
        
        self.display_utils.print_section_header("Keyword Search (Top 3)")
        print(f"🔍 Query: '{query}'\n")
        self.display_utils.print_result(results_3)

        # Then with 500 results and rerank
        results_500 = self.search_utils.keyword_search(
            query,
            self.weaviate_service.client,
            num_results=500
        )
        
        if results_500:
            texts = [result.get('text', '') for result in results_500]
            reranked = self.cohere_service.rerank_responses(query, texts)
            
            # Original version (for debugging)
            self.display_utils.print_section_header("Keyword Search with ReRank (Debug)")
            for i, result in enumerate(reranked):
                print(f"Debug #{i+1}:")
                print(result)
                self.display_utils.print_divider("-", 30)
                
            # User friendly version
            self.display_utils.print_section_header("Keyword Search with ReRank")
            self.display_utils.print_reranked_results(query, reranked, texts, results_500)

    def demonstrate_dense_retrieval_with_rerank(self):
        """Step 4: Demonstrate Dense Retrieval with ReRank"""
        query = "Who is the tallest person in history?"
        results = self.search_utils.dense_retrieval(query, self.weaviate_service.client)
        
        if results:
            texts = [result.get('text', '') for result in results]
            reranked = self.cohere_service.rerank_responses(query, texts)
            
            # Original version (for debugging)
            self.display_utils.print_section_header("Dense Retrieval with ReRank (Debug)")
            for i, result in enumerate(reranked):
                print(f"Debug #{i+1}:")
                print(result)
                self.display_utils.print_divider("-", 30)
                
            # User friendly version
            self.display_utils.print_section_header("Dense Retrieval with ReRank")
            self.display_utils.print_reranked_results(query, reranked, texts, results)

if __name__ == "__main__":
    app = ReRankApp()
    
    # Follow the original flow
    app.demonstrate_dense_retrieval()
    app.demonstrate_keyword_search_with_rerank()
    app.demonstrate_dense_retrieval_with_rerank() 