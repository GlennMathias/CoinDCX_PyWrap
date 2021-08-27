import requests
import time
import json
import hmac
import hashlib
from Auth import Authentication
from Market import Market

class User(Authentication,Market):
    base_url=r'https://api.coindcx.com'
    users_url=r'/exchange/v1/users'
    balance_url=r'/balances'
    info_url=r'/info'
    order_url=r'/exchange/v1/orders'
    create_url=r'/create'
    trade_hist_url=r'/trade_history'
    cancel_url=r'/cancel'
    cancel_all_url=r'/cancel_all'

    def __init__(self,key,secret):
        self.key=key
        self.secret=secret

        
    def getInfo(self):
        # we get secret bytes, get timestamp and save it in a body.
        body=dict()
        json_body,headers=Authentication.authenticate(self,body)
        response=requests.post(self.base_url+self.users_url+self.info_url,data=json_body,headers=headers)
        return response.json()

    def getBalances(self,coins):
        body=dict()
        json_body,headers=Authentication.authenticate(self,body)
        response=requests.post(self.base_url+self.users_url+self.balance_url,data=json_body,headers=headers)
        coin_list=response.json()
        coins_list=[]
        
        if coins==[]:
            return [x for x in coin_list if x['balance'] != '0.0' ]
        else:
            for coin in coin_list:
                if coin['currency'] in coins:
                    coins_list.append(coin)
            return coins_list

        
    def buy(self,market,qty=0,amount=0,order_type='market_order',price_per_unit=0,eode='I'):
        if qty == 0:
            if amount == 0:
                raise ValueError
            coin_price=float(self.getMarketData(market)['last_price'])
            qty=amount/coin_price
        
        body={
            "side":"buy",
            "order_type": order_type,
            "market": market,
            "total_quantity": qty,
            "ecode":eode
            }

        if order_type == 'limit_order' and not price_per_unit == 0:
            body['price_per_unit']=price_per_unit

        json_body,headers=Authentication.authenticate(self,body)
        #res=requests.post(self.base_url+self.order_url+self.create_url,data=json_body,headers=headers)
        res=json_body
        print(res,headers)
        return res

    def sell(self,market,qty,order_type='market_order',price_per_unit=0,ecode='I'):
        body={
            "side":"sell",
            "order_type": order_type,
            "market": market,
            "total_quantity": qty,
            "ecode":eode
            }

        if order_type == 'limit_order' and not price_per_unit == 0:
            body['price_per_unit']=price_per_unit

        json_body,headers=Authentication.authenticate(self,body)
        #res=requests.post(self.base_url+self.order_url+self.create_url,data=json_body,headers=headers)
        res=json_body
        print(res,headers)
        return res


    def getTradeHistory(self,limit=500,trade_id=0,timestamp=0):
        body={'limit':limit}
        if not trade_id==0:
            body['trade_id']=trade_id

        if not timestamp == 0:
            body['timestamp']=timestamp;
            time_flag=False
        else:
            time_flag=True

        json_body,headers=Authentication.authenticate(self,body,time_flag)
        res=requests.post(self.base_url+self.order_url+self.trade_hist_url,data=json_body,headers=headers)
        #print(body)
        return res

    def cancelOrder(self,order_id,timeStamp):
        body={
                'order_id':order_id,
                'timestamp':timeStamp
                }

        json_body,headers=Authentication.authenticate(self,body)
        res=requests.post(self.base_url+self.order_url+self.cancel_url,data=json_body,headers=headers)
        return res

    def getHeldAmount(self,coin,currency):
        btc_price=float(self.getMarketData(coin+currency)['last_price'])
        btc_holding=float(self.getBalances([coin])[0]['balance'])

        return btc_price*btc_holding

    #Not Sure
    def sellAll(self):
        for orders in self.ordersPlaced():
            self.sell(orders)






































        
