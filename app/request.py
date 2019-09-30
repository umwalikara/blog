# import json
# import requests
# from .models import Quotes
# from config import Config

# base_url = None

# def configure_request(app):
#     global base_url
# base_url = Config.QUOTES_API_BASE_URL

# def get_quotes():
#     '''
#     function that gets json response to our url request
#     '''
#     quote_object = requests.get(base_url) #to get quote url
#     new_quote = quote_object.json() # in getting objects in json format
#     author = new_quote.get("author")
#     quote = new_quote.get("quote")
#     object = Quotes(author,quote)

#     return object