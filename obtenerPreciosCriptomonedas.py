import requests
import time
from datetime import datetime

headers = {
        'X-CMC_PRO_API_KEY': 'eea2da26-3b5c-4c3c-aad3-49b26bd48217',
        'Accepts': 'application/json'
        }

params = {
        'start': '1',
        'limit': '5000',
        'convert': 'EUR'
        }

archivo = open

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = params, headers = headers).json()

coins =  json['data']
now = datetime.now()
print('Movimientos Bego a día ' + str(now.date()) + ' a las ' + str(now.time()) +'\n') 
for coin in coins:
	# CRYPTO.COM
	if coin['name'] == 'Crypto.com Coin':
		CRO = 307.6*coin['quote']['EUR']['price']
	if coin['name'] == 'PancakeSwap':
		CAKE = 1.139*coin['quote']['EUR']['price']
	if coin['name'] == 'Polkadot':
		DOT = 1.139*coin['quote']['EUR']['price']
	#DIGIFINEX
	if coin['name'] == 'Jobchain':
		JOB = 603480*coin['quote']['EUR']['price']
	#COINBASE
	if coin['name'] == 'Cosmos':
		ATOM = 2.179654*coin['quote']['EUR']['price']
	if coin['name'] == 'Amp':
		AMP = 52.76116779*coin['quote']['EUR']['price']
	if coin['name'] == 'BarnBridge':
		BOND = 0.0712251*coin['quote']['EUR']['price']
print('a) Crypto.com: \n 1) CRO -->' + str(CRO) + '€ \n 2) CAKE -->' + str(CAKE) + '€ \n 3) DOT -->' + str(DOT) + '€ \n')
print('b) Digifinex: \n 1) JOB -->' + str(JOB) + '€ \n')
print('c) Coinbase: \n 1) ATOM -->' + str(ATOM) + '€ \n 2) AMP -->' + str(AMP) + '€ \n 3) BOND -->' + str(BOND) + '€ \n')
print('ACTIVO TOTAL: ' + str(round(CRO+CAKE+DOT+JOB+ATOM+AMP+BOND,2)) + '€')

