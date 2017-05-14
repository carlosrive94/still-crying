import urllib
import BeautifulSoup
import json

urls = [
    'https://blockchain.info/address/13AM4VW2dhxYgXeQepoHkHSQuy6NgaEb94',
    'https://blockchain.info/address/115p7UMMngoj1pMvkpHijcRdfJNXj6LrLn',
    'https://blockchain.info/address/12t9YDPgwueZ9NyMgw519p7AA8isjr6SMw'
]
totalBitcoins = 0
for url in urls:
    f = urllib.urlopen(url)
    soup = BeautifulSoup.BeautifulSoup(f.read())
    val = soup.find('td', {'id': 'total_received'}).span.string.split(' ')[0]
    totalBitcoins += float(val)

f = urllib.urlopen('http://api.coindesk.com/v1/bpi/currentprice.json')
resp = json.loads(f.read())
eurConversion = float(resp['bpi']['EUR']['rate_float'])
eurTotal = eurConversion * totalBitcoins
print('Total earned: ' + str(eurTotal) + ' euros')
