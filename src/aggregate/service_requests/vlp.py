from aggregate.config import Settings
import httpx


async def calc_vlp(json_data):
    async with httpx.AsyncClient() as client:
        return await client.post(
            Settings.VLP_HOST.value + "/vlp/calculator", json=json_data, timeout=None
        )
