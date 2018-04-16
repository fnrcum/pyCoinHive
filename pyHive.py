from urllib import parse
import requests
import json

"""
This is a python implementation of the CoinHiveApi class provided by CoinHive from PHP in Python3
"""


class CoinHiveAPI(object):

    API_URL = 'https://api.coinhive.com'
    secret = None

    def __init__(self, secret):
        if len(secret) != 32:
            raise Exception('CoinHive - Invalid Secret')

        self.secret = secret

    def get(self, path, data={}):
        data['secret'] = self.secret
        url = self.API_URL + path + '?' + parse.urlencode(data)
        print(url)
        response = requests.get(url)
        return json.loads(response.text)

    def post(self, path, data={}):
        data['secret'] = self.secret
        print(data)
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        url = self.API_URL + path
        response = requests.post(url, headers=headers, data=data)
        return json.loads(response.text)