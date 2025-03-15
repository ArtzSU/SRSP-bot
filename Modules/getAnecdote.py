import asyncio
import aiohttp
from bs4 import BeautifulSoup

import random
import logging

URL = 'https://nekdo.ru/random/'
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

JOKES_list = [
    '''— Доктор, у меня проблема: я всё время забываю, что хотел сказать.
— Сколько это уже продолжается?
— Что «это»?''',

    '''— Почему вы опоздали на работу?
— Проспал.
— И что, до 16:00 спали?
— Нет, до 15:55.''',

    '''— Папа, а кто такой пессимист?
— Это человек, который, когда ему дают выбор между двумя злами, выбирает оба.''',
]

def findInSoup(soup: BeautifulSoup):
    element = soup.find('div', id=True, class_=True)
    return element

async def getAnecdote() -> str:
    logging.info("Запрашиваю анекдот с сайта.")
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        try:
            async with session.get(URL) as response:
                if response.status == 200:
                    logging.info("Успешно получен ответ от сервера.")
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')

                    element = findInSoup(soup)
                    if element:
                        logging.info("Анекдот успешно найден на странице.")
                        return element.text.strip()

                logging.warning(f"Получен неудачный статус ответа: {response.status}. Использую локальный анекдот.")
                return random.choice(JOKES_list)
        except Exception as e:
            logging.error(f"Ошибка при запросе: {e}. Использую локальный анекдот.")
            return random.choice(JOKES_list)

if __name__ == "__main__":
    async def main():
        text = await getAnecdote()
        print(text)

    asyncio.run(main())