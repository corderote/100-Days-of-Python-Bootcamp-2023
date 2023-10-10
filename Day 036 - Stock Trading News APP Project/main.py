# ----------------------------------------------------------------------------- #
import requests

STOCK_NAME = "IBM"
COMPANY_NAME = "IBM"

ALPHA_ADVANTAGE_API_URL = "https://www.alphavantage.co/query"
# You should provide your own key here, use it from code or from your environment,
# The one used here is set to be a placeholder, will not work.
ALPHA_ADVANTAGE_API_KEY = "alpha_advantage_api_key"

ALPHA_ADVANTAGE_API_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_ADVANTAGE_API_KEY,
}

NEWS_API_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "news_api_key"

NEWS_API_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

alpha_api_response = requests.get(ALPHA_ADVANTAGE_API_URL, params=ALPHA_ADVANTAGE_API_PARAMS)
alpha_api_response.raise_for_status()

# Check alpha advantage documentation to understand how we are dealing with the data
# from the response to use it as we want to.

alpha_api_data = alpha_api_response.json()
data_list = [value for (key, value) in alpha_api_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
dby_closing_price = data_list[1]["4. close"]

difference_between_closing_prices = abs(float(yesterday_closing_price) - float(dby_closing_price))

diff_percentage = (difference_between_closing_prices / float(yesterday_closing_price)) * 100

if diff_percentage > 5.0:
    news_api_response = requests.get(NEWS_API_URL, params=NEWS_API_PARAMS)
    news_api_response.raise_for_status()

    news_api_data = news_api_response.json()

    # Get hold of the 3 first articles from the news API.
    articles = news_api_data["articles"][:3]

    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in articles]

# To end the project you can use yesterday's lesson to send the articles via
# Twilio or send an email using smtplib or using the resend API.
# ----------------------------------------------------------------------------- #
