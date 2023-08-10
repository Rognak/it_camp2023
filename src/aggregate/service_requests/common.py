# import asyncio
# from urllib.parse import urljoin
#
# import httpx
#
#
# # def asynchronized(func):
# #     async def wrapped(*args, **kwargs):
# #         loop = asyncio.get_event_loop()
# #         combined_args = args + tuple(kwargs.values())
# #         res = await loop.run_in_executor(None, func, *combined_args)
# #         return res
# #
# #     return wrapped
#
#
# #@asynchronized
# def post(host, url, json_data=None):
#     return httpx.post(urljoin(host, url), json=json_data)
