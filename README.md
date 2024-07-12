Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/your-repo.git
cd your-repo
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the FastAPI application using Uvicorn:

bash
Copy code
uvicorn api:app --reload
Replace api with the actual filename (excluding the .py extension) if your file has a different name.

Access the API documentation:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Use the API to get cryptocurrency information and analysis:

Example Request:

bash
Copy code
curl -X 'GET' \
  'http://127.0.0.1:8000/crypto/BTC' \
  -H 'accept: application/json'
Response:

json
Copy code
{
  "name": "Bitcoin",
  "symbol": "BTC",
  "current_price_usd": 50000.0,
  "analysis": "Your generated analysis text here."
}



Copy code
# CoinMarketCap API Key (Replace with your API key)
# CoinMarketCap API Key (Replace with your API key)
coinmarketcap_api_key = '03de30d4-2a16-4685-8179-ea9590801402'

# OpenAI API Key (Replace with your API key)
openai.api_key = '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'

# OpenAI API Key (Replace with your API key)
