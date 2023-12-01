import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class NewsAPIView(APIView):
    def get(self, request):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list"
        querystring = {"region":"US","snippetCount":"28"}
        payload = "Pass in the value of uuids field returned right in this endpoint to load the next page, or leave empty to load first page"
        headers = {
            "content-type": "text/plain",
            "X-RapidAPI-Key": "d1361dddfamshb19e08e63c9b86dp1fe0e4jsnf934221382e3",
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        response = requests.post(url, data=payload, headers=headers, params=querystring)
        return Response(response.json())

class NewsDetail(APIView):
    def get(self, request, uuid):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"
        querystring = {"uuid": uuid, "region": "US"}
        headers = {
            "X-RapidAPI-Key": "d1361dddfamshb19e08e63c9b86dp1fe0e4jsnf934221382e3",
            "X-RapidAPI-Host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        return Response(response.json())
