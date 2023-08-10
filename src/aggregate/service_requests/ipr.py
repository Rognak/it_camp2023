from aggregate.config import Settings
import httpx


async def calc_ipr(json_data):
    async with httpx.AsyncClient() as client:
        res = await client.post(Settings.IPR_HOST.value + "/ipr/calc", json=json_data)
    return res
