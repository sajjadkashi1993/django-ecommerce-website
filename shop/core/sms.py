import requests
import json


class APIException(Exception):
    pass

class HTTPException(Exception):
    pass

class SmsAPI():
    def __init__(self, apikey):
        self.version = 'v1'
        self.host = 'api.sms.ir'
        self.apikey = apikey
        self.headers = {
	    'Accept': 'text/plain',
	    'Content-Type': 'application/json',
	    'charset': 'utf-8',
        'x-api-key':self.apikey
            }
        
    def __repr__(self):
        return "sms.SmsAPI({!r})".format(self.apikey)

    def __str__(self):
        return "sms.SmsAPI({!s})".format(self.apikey)

    def _request(self, action, method, params={}):
        url = 'https://' + self.host + '/' + self.version + '/' + method + '/' + action 
        try:
            content = requests.post(url , headers=self.headers,json=params).content
            try:
                response = json.loads(content.decode("utf-8"))
                if (response['status']==1):
                    response=response['message']
                elif(response['status']==102):
                    response=response['message']
                else:
                    raise APIException((u'APIException[%s]' % (response['status'])).encode('utf-8'))
            except ValueError as e:
                raise HTTPException(e)
            return (response)
        except requests.exceptions.RequestException as e:
            raise HTTPException(e)
        
    def sms_verify_send(self, params=None):
        return self._request('verify', 'send',params)
     
