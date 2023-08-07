import httpx
import asyncio
import re

async def request(client=httpx.AsyncClient()):
    URL = "http://watcher:8668/one"
    print("Trying to connect " + URL )
    response = await client.get(URL)
    response_s = re.sub(r'\\\"', '"', response.text)
    return response_s

async def reconnect(client=httpx.AsyncClient()):
    URL = "http://watcher:8668/reconnect"
    response = await client.get(URL)
    text = response.text
    if text == '{"Result":"Success"}':
        return 'success'
    else:
        return 'error'
    