import requests

VIOTP_API_KEY = '4737b2d378624a90a303752b3122c679'

class Viotp:
    def __init__(self, id_service) -> None:
        self.id_service = id_service
        self.phone_number = None
        self.request_id = None
        self.result_code = None
        self.response_message = None
        
    def getPhoneNumber(self) -> None:
        r = requests.get(f'https://api.viotp.com/request/getv2?token={VIOTP_API_KEY}&serviceId={self.id_service}').json()
        if r['status_code'] == 200:
            self.phone_number = r['data']['phone_number']
            self.request_id = r['data']['request_id']

    def getResult(self) -> None:
        r = requests.get(f'https://api.viotp.com/session/getv2?requestId={self.request_id}&token={VIOTP_API_KEY}').json()
        if r['status_code'] == 200:
            try:
                self.result_code = r['Code']
                self.response_message = r['SmsContent']
            except:
                pass
    
    def cancelRent(self) -> None:
        pass
  
    def __str__(self) -> None:
        return f'{self.phone_number}\n{self.request_id}\n{self.result_code}\n{self.response_message}'
                


if __name__ == '__main__':
    x = Viotp(5)
    x.getPhoneNumber()
    while(True):
        
        x.getResult()
        print(x)