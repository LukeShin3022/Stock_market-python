from django.shortcuts import render
# from django.http import HttpResponse
import requests
import json

# Create your views here.

def home(request):

    stock_api = requests.get("https://api.iex.cloud/v1/data/core/quote/aapl?token=pk_15d00f092312459c9a17a01edb0f1e47")
    stock = json.loads(stock_api.content)
    content = {'stock':stock}
    return render(request,'stocks/home.html',content)
