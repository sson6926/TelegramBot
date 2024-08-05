import aiohttp
import asyncio

VIOTP_API_KEY = None

class Viotp:
    def __init__(self, id_service) -> None:
        self.id_service = id_service
        self.phone_number = None
        self.request_id = None
        self.result_code = None
        self.response_message = None

    async def getPhoneNumber(self) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.viotp.com/request/getv2?token={VIOTP_API_KEY}&serviceId={self.id_service}') as response:
                r = await response.json()
                if r['status_code'] == 200:
                    self.phone_number = r['data']['phone_number']
                    self.request_id = r['data']['request_id']

    async def getResult(self) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.viotp.com/session/getv2?requestId={self.request_id}&token={VIOTP_API_KEY}') as response:
                r = await response.json()
                if r['status_code'] == 200:
                    try:
                        self.result_code = r['Code']
                        self.response_message = r['SmsContent']
                    except KeyError:
                        pass

    async def cancelRent(self) -> None:
        pass

    def __str__(self) -> str:
        return f'{self.phone_number}\n{self.request_id}\n{self.result_code}\n{self.response_message}'