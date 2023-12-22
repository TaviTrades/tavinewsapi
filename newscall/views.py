from django.core.cache import cache
from datetime import timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from dotenv import load_dotenv
import os

load_dotenv()

RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')

class NewsAPIView(APIView):
    def get(self, request):
        cached_data = cache.get('news_list')
        if not cached_data:
            # Your existing code to fetch data from the API
            url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list"
            querystring = {"region":"US","snippetCount":"28"}
            payload = "Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page"
            headers = {
                "content-type": "text/plain",
                "X-RapidAPI-Key": RAPIDAPI_KEY,
                "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }
            response = requests.post(url, data=payload, headers=headers, params=querystring)
            cached_data = response.json()
            # Cache the data for 12 hours
            cache.set('news_list', cached_data, timeout=43200) 
        return Response(cached_data)
    
class NewsDetail(APIView):
    def get(self, request, uuid):
        cache_key = f'news_detail_{uuid}'
        cached_data = cache.get(cache_key)
        
        if not cached_data:
            url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"
            querystring = {"uuid": uuid, "region": "US"}
            headers = {
                "X-RapidAPI-Key": RAPIDAPI_KEY,
                "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            cached_data = response.json()
            # Cache the data for 12 hours
            cache.set(cache_key, cached_data, timeout=43200)
        
        return Response(cached_data)

