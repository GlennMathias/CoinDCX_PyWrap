import time
import json
import hmac
import hashlib

class Authentication():

    def __init__(self):
        pass

        # we get secret bytes, get timestamp and save it in a body.

    def authenticate(self,body,time_flag=False):
        timeStamp=int(round(time.time()*1000))
        body["timestamp"]=timeStamp

        #save body as json

        json_body=json.dumps(body,separators=(',',':'))
        secret_bytes = bytes(self.secret, encoding='utf-8')
        signature=hmac.new(secret_bytes,json_body.encode(),hashlib.sha256).hexdigest()
        
        headers={
                    'Content-Type': 'application/json',
                    'X-AUTH-APIKEY': self.key,
                    'X-AUTH-SIGNATURE': signature
                }
        return json_body,headers
