# Keyword + Dense Retrieval + ReRank

A modular Python application that demonstrates different search approaches using Weaviate vector database and Cohere's reranking capabilities.

## 🌟 Features

- **Dense Retrieval**: Vector-based semantic search using Weaviate
- **Keyword Search**: Traditional BM25-based search
- **ReRanking**: Enhanced search results using Cohere's reranking model
- **Multiple Display Formats**: Both debug and user-friendly output options

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Weaviate Cloud Instance
- Cohere API Key

### Installation

1. Clone the repository: 


2. Install required packages:

```
bash
pip install -r requirements.txt
```


3. Create a `.env` file in the root directory with your API keys:

```
COHERE_API_KEY=your_cohere_key
WEAVIATE_API_KEY=your_weaviate_key
WEAVIATE_API_URL=your_weaviate_url
```


### Running the Application

```
python main.py
```


## 📁 Project Structure

project/
├── .env # Environment variables
├── requirements.txt # Project dependencies
├── main.py # Main application file
├── config/
│ └── settings.py # Configuration settings
├── services/
│ ├── cohere_service.py # Cohere API integration
│ └── weaviate_service.py # Weaviate API integration
└── utils/
├── search.py # Search utilities
├── display.py # Display formatting
└── schema_setup.py # Database schema setup


## 🔍 Features in Detail

### Dense Retrieval
- Performs semantic search using vector embeddings
- Returns the most semantically similar results

### Keyword Search with ReRank
1. Initial keyword search with BM25 algorithm
2. Retrieves top 500 results
3. Reranks results using Cohere's model
4. Displays results with relevance scores

### Dense Retrieval with ReRank
- Combines vector search with reranking
- Optimizes results for both semantic similarity and relevance

## 📊 Output Format

The application provides two types of output for each search:

1. **Debug Version**
   - Raw data format
   - Complete response information
   - Technical details

2. **User-Friendly Version**
   - Clean, formatted output
   - Relevance scores
   - Easy-to-read result hierarchy
   - Emoji indicators for different sections

## 🔑 API Keys

The application requires three API keys:
- Cohere API Key
- Weaviate API Key
- Weaviate API URL

Store these in your `.env` file and never commit them to version control.

## 🛠️ Development

To add new features:
1. Create appropriate modules in the relevant directories
2. Update the main application class
3. Add any new requirements to `requirements.txt`
4. Update documentation as needed

## ⚠️ Important Notes

- Keep your API keys secure
- The free tier of services may have rate limits
- Sample data is automatically added on first run

## 📝 License

[Add your license information here]
