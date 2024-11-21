class SearchUtils:
    @staticmethod
    def dense_retrieval(query, weaviate_client):
        """Perform dense retrieval using Weaviate"""
        try:
            response = (
                weaviate_client.query
                .get("Article", ["text", "title", "url", "views", "lang"])
                .with_near_text({"concepts": [query]})
                .with_limit(3)  # Default to 3 results like original
                .do()
            )
            
            if response and "data" in response and "Get" in response["data"]:
                return response["data"]["Get"]["Article"]
            return []
            
        except Exception as e:
            print(f"Error in dense_retrieval: {e}")
            return []

    @staticmethod
    def keyword_search(query, weaviate_client, properties=None, num_results=3):
        """Perform keyword search using Weaviate's BM25"""
        if properties is None:
            properties = ["text", "title", "url", "views", "lang", "_additional {distance}"]
        
        try:
            response = (
                weaviate_client.query
                .get("Article", properties)
                .with_bm25(query=query)
                .with_limit(num_results)
                .do()
            )
            
            if response and "data" in response and "Get" in response["data"]:
                return response["data"]["Get"]["Article"]
            return []
            
        except Exception as e:
            print(f"Error in keyword_search: {e}")
            return []