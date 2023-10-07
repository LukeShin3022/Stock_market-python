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
        url = f"{self.BASE_URL}/stock/{self.symbol}/logo?token={config_e.IEX_TOKEN}"
        r = requests.get(url)

        return r.json()

    def get_company_info(self):
        url = f"{self.BASE_URL}/data/core/company/{self.symbol}?token={config_e.IEX_TOKEN}"
        r = requests.get(url)

        return r.json()

