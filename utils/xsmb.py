import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json


async def getSXMB():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://az24.vn/xsmb-sxmb-xo-so-mien-bac.html") as response:
                r = await response.text()

        soup = BeautifulSoup(r, 'html.parser')
        date = soup.select("#kqmb_0 > div.tit-mien.clearfix.txt-center > div > a:nth-child(3)")[
            0].get_text().replace("XSMB ng\u00e0y ", "")
        g_db = soup.select(
            "#load_kq_mb_0 > div.one-city > table > tbody > tr.db > td.v-giai.number > span")[0].get_text()
        g_1 = soup.select(
            "#load_kq_mb_0 > div.one-city > table > tbody > tr:nth-child(3) > td.v-giai.number > span")[0].get_text()
        g_2 = [i.get_text() for i in soup.select(
            "#load_kq_mb_0 > div.one-city > table > tbody > tr:nth-child(4) > td.v-giai.number > span")]
        g_3 = [i.get_text() for i in soup.select(
            "#load_kq_mb_0 > div.one-city > table > tbody > tr:nth-child(5) > td.v-giai.number > span")]
        g_4 = [i.get_text() for i in soup.select(
            "#load_kq_mb_0 > div.one-city > table > tbody > tr:nth-child(6) > td.v-giai.number > span")]
        g_5 = [i.get_text() for i in soup.select(
            "#load_kq_mb_0 > div.one-city > table > tbody > tr:nth-child(7) > td.v-giai.number > span")]
        g_6 = [i.get_text() for i in soup.select(
            "#load_kq_mb_0 > div.one-city > table > tbody > tr:nth-child(8) > td.v-giai.number > span")]
        g_7 = [i.get_text() for i in soup.select(
            "#load_kq_mb_0 > div.one-city > table > tbody > tr.g7 > td.v-giai.number > span")]

        if len(g_7) == 4:
            return json.dumps({"status": 200, "date": date, "data": {"giai_dac_biet": g_db, "giai_1": g_1, "giai_2": g_2, "giai_3": g_3, "giai_4": g_4, "giai_5": g_5, "giai_6": g_6, "giai_7": g_7}})
    except Exception as e:
        return json.dumps({"status": 400, "msg": "could not fetch data", "error": str(e)})