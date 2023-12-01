from django.core.management.base import BaseCommand
from .models import News
import requests

class Command(BaseCommand):
    help = 'Fetches news from the API'

    def handle(self, *args, **options):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list"
        querystring = {"region":"US","snippetCount":"28"}
        payload = "Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page"
        headers = {
            "content-type": "text/plain",
            "X-RapidAPI-Key": "d1361dddfamshb19e08e63c9b86dp1fe0e4jsnf934221382e3",
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }

        response = requests.post(url, data=payload, headers=headers, params=querystring)
        News.objects.create(data=response.json())
