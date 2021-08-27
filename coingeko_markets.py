import requests

base_url=r'https://api.coingecko.com/api/v3/coins'
list_uri=r'/list'

def getCoinList(start,end):
    url=base_url+r'/list'
    res=requests.get(url)
    data=res.json()
    return data[start:end]
    

def getHistoricalData(coin,days,interval='',currency="inr"):
    url=base_url+f'/{coin}/market_chart?vs_currency={currency}&days={days}'
    if interval != '':
        url+='&interval={interval}'
    res=requests.get(url)
    data=res.json()
    prices=[y for x,y in data['prices']]
    timestamp=[x for x,y in data['prices']]
    return timestamp,prices

def getName(symbol):
    res=getCoinList(0,-1)
    for r in res:
        if r["symbol"]== symbol.lower():
            print(r['id'])
            break

    return r['id']


if __name__=="__main__":
    '''
    
    import matplotlib.pyplot as plt

    coin_list=getCoinList(0,-1)
    for coin in coin_list:
        if coin['id'].startswith('c'):
            print(coin['id'])

    currency=input("Enter currency: ")
    
    x,prices=getHistoricalData(currency,1000)
    #x=[i for i in range(len(prices))]
    plt.plot(x,prices)
    plt.show()
    '''
    

    #print(res[0:34])
    
