from django.shortcuts import render
# from django.http import HttpResponse
import requests
import json

# Create your views here.

def home(request):

    try:
        ticker = request.GET['ticker']
        stock_api = requests.get("https://api.iex.cloud/v1/data/core/quote/" + ticker + "?token=pk_15d00f092312459c9a17a01edb0f1e47")
        stock = json.loads(stock_api.content)
    except Exception as e:
        stock = ""


    content = {'stock':stock}
    return render(request,'stocks/home.html',content)
