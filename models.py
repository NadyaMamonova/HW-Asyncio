import aiohttp
import asyncio


url = 'http://swapi.dev/api/people/'


async def get_person(session, url):
    async with session.get(url) as file:
        return await file.json()


async def get_name(url):
    async with aiohttp.ClientSession() as session:
        async  for page in range(1, 100):
            data = await get_person(session, url)
            return data



if __name__ == '__main__':
    asyncio.run(main())
