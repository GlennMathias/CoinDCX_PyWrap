import requests
class Market:
    base_url= r'https://public.coindcx.com'
    ticker_url = r"/exchange/ticker"
    candles_url= r"/market_data/candles"
    def getMarketData(self,coin_needed):
        res=requests.get(self.base_url+self.ticker_url)
        coins_data=[]
        for coin in res.json():
            if coin['market'] == coin_needed:
                return coin

    def getCandles(self,coin_pair,interval,limit=500,ecode='B'):
        url=self.base_url+self.candles_url+f'?pair={ecode}-{coin_pair}&interval={interval}&limit={limit}'
        res=requests.get(url)    
        data=res.json()
        return data

if __name__=="__main__":
    mar=Market()
    mar.getCandles('BTC_USDT',"1m")
