def create_schema(weaviate_client):
    """Create the schema for the Article class if it doesn't exist"""
    
    # First check if the schema already exists
    try:
        schema = weaviate_client.schema.get()
        if any(class_obj['class'] == 'Article' for class_obj in schema['classes']):
            print("Schema already exists")
            return
    except Exception as e:
        print(f"Error checking schema: {e}")
        return

    # Define the schema for Article class
    schema = {
        "class": "Article",
        "description": "A Wikipedia article",
        "vectorizer": "text2vec-cohere",  # Use Cohere for vectorization
        "moduleConfig": {
            "text2vec-cohere": {
                "model": "embed-english-v2.0",
                "truncate": "RIGHT"
            }
        },
        "properties": [
            {
                "name": "title",
                "dataType": ["text"],
                "description": "Title of the article"
            },
            {
                "name": "text",
                "dataType": ["text"],
                "description": "Main content of the article"
            },
            {
                "name": "url",
                "dataType": ["text"],
                "description": "URL of the article"
            },
            {
                "name": "views",
                "dataType": ["int"],
                "description": "Number of views"
            },
            {
                "name": "lang",
                "dataType": ["text"],
                "description": "Language of the article"
            }
        ]
    }

    try:
        weaviate_client.schema.create_class(schema)
        print("Schema created successfully")
    except Exception as e:
        print(f"Error creating schema: {e}") 