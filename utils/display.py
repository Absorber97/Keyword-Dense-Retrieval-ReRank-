class DisplayUtils:
    @staticmethod
    def print_divider(char="=", length=50):
        print(f"\n{char * length}\n")
    
    @staticmethod
    def print_section_header(title):
        print(f"\n{'='*50}")
        print(f"📌 {title}")
        print(f"{'='*50}\n")
    
    @staticmethod
    def print_result(results):
        if not results:
            print("❌ No results found.")
            return
            
        for i, result in enumerate(results):
            print(f"📎 Result #{i+1}")
            print(f"   Title: {result.get('title', 'No title')}")
            print(f"   Text: {result.get('text', 'No text')}")
            if result.get('url'):
                print(f"   URL: {result.get('url')}")
            print()

    @staticmethod
    def print_reranked_results(query, reranked, texts, original_results):
        """Print reranked results in a user-friendly format"""
        if not hasattr(reranked, 'results'):
            print("❌ No reranked results available")
            return
            
        print(f"🔍 Query: '{query}'")
        print(f"📊 Found {len(reranked.results)} relevant results\n")
        
        for i, rerank_result in enumerate(reranked.results):
            # Get original content
            original_text = texts[rerank_result.index]
            original_result = original_results[rerank_result.index]
            
            # Print result with proper indentation and formatting
            print(f"{'─'*40}")  # Separator between results
            print(f"📎 Result #{i+1}")
            print(f"   Relevance Score: {rerank_result.relevance_score:.2%}")
            print(f"   Title: {original_result.get('title', 'No title')}")
            print(f"   Text: {original_text}")
            print(f"   URL: {original_result.get('url', 'No URL')}")
            print() 