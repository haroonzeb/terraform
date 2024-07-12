from fastapi import FastAPI, HTTPException
import openai
import httpx
import datetime

app = FastAPI()

# CoinMarketCap API Key (Replace with your API key)
coinmarketcap_api_key = '03de30d4-2a16-4685-8179-ea9590801402'

# OpenAI API Key (Replace with your API key)
openai.api_key = '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'

# Function to retrieve cryptocurrency data from CoinMarketCap
def get_crypto_data(crypto_name):
    base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {
        "symbol": crypto_name,
        "convert": "USD",
    }
    headers = {
        "X-CMC_PRO_API_KEY": coinmarketcap_api_key,
    }
    with httpx.Client() as client:
        response = client.get(base_url, params=params, headers=headers)
    data = response.json()
    return data['data'][crypto_name]

# Function to generate analysis using ChatGPT
def generate_analysis(crypto_name, price):
    # Get the current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prompt = f"Your job is to provide predictions and analysis for {crypto_name} cryptocurrency based on technical analysis and fundamental analysis keeping the latest crypto trends and news in context for your decision.\nPrice: ${price}\nAlso, suggest target prices for short and long-term holding.\nAnalysis generated on: {current_datetime}"

    # Ask ChatGPT for technical analysis, fundamental analysis, and price prediction
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate model for your use case
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,  # Adjust the max tokens to control response length
        stop=None,
        temperature=0.7,
    )

    return response['choices'][0]['message']['content'].strip()
# FastAPI route to get cryptocurrency information and analysis
@app.get("/crypto/{crypto_name}")
def get_crypto_analysis(crypto_name: str):
    try:
        crypto_data = get_crypto_data(crypto_name)
        analysis = generate_analysis(crypto_name, crypto_data['quote']['USD']['price'])
        return {"name": crypto_data['name'],
                "symbol": crypto_data['symbol'],
                "current_price_usd": crypto_data['quote']['USD']['price'],
                "analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

# FastAPI route to get cryptocurrency metadata
@app.get("/metadata/{crypto_name}")
def get_crypto_metadata_route(crypto_name: str):
    try:
        crypto_metadata = get_crypto_metadata(crypto_name)
        return {"name": crypto_metadata['name'],
                "symbol": crypto_metadata['symbol'],
                "description": crypto_metadata['description'],
                # Add more fields as needed
                }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


@app.get("/chat/{user_message}")
def chat_with_gpt(user_message: str):
    try:
        # Use the OpenAI Chat API directly
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the appropriate model for your use case
            messages=[
                {"role": "system", "content": "You are a helpful assistant for technichal and fundamental analysis for cypto and you should strictly only discuss things related to it ."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=300,  # Adjust the max tokens to control response length
            stop=None,
            temperature=0.7,
        )

        return {"response": response['choices'][0]['message']['content'].strip()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
    



    # FastAPI route to get cryptocurrency information and analysis
@app.get("/crypto/{crypto_name}")
def get_crypto_analysis(crypto_name: str):
    try:
        crypto_data = get_crypto_data(crypto_name)
        analysis = generate_analysis(crypto_name, crypto_data['quote']['USD']['price'])
        return {"name": crypto_data['name'],
                "symbol": crypto_data['symbol'],
                "current_price_usd": crypto_data['quote']['USD']['price'],
                "analysis": analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")

@app.get("/info/{crypto_name}")
def get_crypto_info(crypto_name: str):
    try:
        crypto_data = get_crypto_data(crypto_name)
        return {"name": crypto_data['name'],
                "symbol": crypto_data['symbol'],
                "current_price_usd": crypto_data['quote']['USD']['price'],
                "market_cap": crypto_data['quote']['USD']['market_cap'],
                # Add more fields as needed
                }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")
    


def get_crypto_metadata(crypto_name):
    base_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/info"
    params = {
        "symbol": crypto_name,
    }
    headers = {
        "X-CMC_PRO_API_KEY": coinmarketcap_api_key,
    }
    with httpx.Client() as client:
        response = client.get(base_url, params=params, headers=headers)
    data = response.json()
    return data['data'][crypto_name]
