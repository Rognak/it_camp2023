from aggregate.config import Settings
import httpx


async def calc_nodal(json_data):
    host = Settings.NODAL_HOST.value
    async with httpx.AsyncClient() as client:
        res = await client.post(host + "/nodal/calc", json=json_data)
    return res
