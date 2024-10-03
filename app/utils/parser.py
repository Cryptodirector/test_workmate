import asyncio
from bs4 import BeautifulSoup as bs
from aiohttp import ClientSession
from typing import AsyncGenerator, Any

from sqlalchemy import insert
from app.database import async_session_maker
from app.models.cat_model import Breed


class Parser:
    url = 'https://www.purina.ru/find-a-pet/cat-breeds'
    lst_breed = []

    @classmethod
    async def pars_site(
            cls
    ) -> AsyncGenerator:
        async with ClientSession() as session:
            for page in range(1, 6):
                async with session.get(
                        cls.url + f'?page={page}'
                ) as response:
                    soup = bs(
                        await response.text(),
                        'html.parser'
                    )
                    cards = soup.find_all(
                        'h4', {'class': 'results-view-name'}
                    )
                    for card in cards:
                        title = card.find('a')
                        cls.lst_breed.append(title.text.strip())
                        yield title.text.strip()

    @classmethod
    async def save_breed(
            cls,
    ) -> Any:
        async with async_session_maker() as session:
            async for title in cls.pars_site():
                await session.execute(
                    insert(Breed).values(title=title)
                )
            await session.commit()


async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(Parser.save_breed())


if __name__ == '__main__':
    asyncio.run(main())
