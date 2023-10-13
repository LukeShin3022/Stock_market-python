import requests
import config_e

class IEXStock:

    def __init__(self, token, symbol, environment='production'):
        if environment == 'production':
            self.BASE_URL = 'https://api.iex.cloud/v1'
        else:
            self.BASE_URL = 'https://sandbox.iexapis.com/v1'
        
        self.token = token
        self.symbol = symbol

    def get_logo(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/logo?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_company_info(self):
        url = f"{self.BASE_URL}/data/core/company/{self.symbol}?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_company_news(self, last=10):
        url = f"{self.BASE_URL}/data/core/company/{self.symbol}/news/last/{last}?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_stats(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/advanced-stats?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_fundamentals(self, period='quarterly', last=4):
        url = f"{self.BASE_URL}/data/core/fundamentals/{self.symbol}/{period}?range={last}&token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_dividends(self, range='5y'):
        url = f"{self.BASE_URL}/stock/{self.symbol}/dividends/{range}?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_institutional_ownership(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/institutional-ownership?token={self.token}"
        r = requests.get(url)

        return r.json()

    def get_insider_transactions(self):
        url = f"{self.BASE_URL}/stock/{self.symbol}/insider-transactions?token={self.token}"
        r = requests.get(url)

        return r.json()

