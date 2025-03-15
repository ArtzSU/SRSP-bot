import asyncio
import logging

from aiogram.filters import Command
from aiogram.enums import ParseMode, ChatType
from aiogram.client.default import DefaultBotProperties
from aiogram import (
    F,
    Bot,
    html,
    Dispatcher,
)
from aiogram.types import (
    Message,
    FSInputFile,
    BotCommand,
)

from Modules.getAnecdote import getAnecdote

import config

from keyboard import main_kb


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG if config.DEBUG else logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

dp = Dispatcher()
bot = Bot(
    token=config.TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)


async def set_commands(service: Bot):
    """
    Регистрация команд бота в меню команд Telegram
    """
    commands = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="help", description="Help"),
        BotCommand(command="team_members", description="Show members of development team"),
        BotCommand(command="documentation", description="Show documentation"),
        BotCommand(command="presentation", description="Show presentation"),
    ]

    await service.set_my_commands(commands)
    logger.info("Команды бота успешно зарегистрированы")



@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    """
    Handler for the `/start` command
    """

    await message.reply(
        text=f"Hello, {html.bold(message.from_user.full_name)}! {await getAnecdote()}",
        reply_markup=main_kb
    )


@dp.message(Command("team_members"))
async def command_of_devers(message: Message):
    """
    Handler for the `/team_members` command
    """

    await message.reply(text=config.TEAM_MEMBERS_STR)


@dp.message(Command("help"))
async def cmd_help(message: Message):
    """
    Handler for the `/help` command
    """

    await message.reply(
        text = """Вот список команд:
/start - начать работу
/help - вывести это сообщение
/documentation - отправляет отчет проделанной работы
/presentation - отправляет презентацию о боте"""

    )


@dp.message(Command("documentation"))
async def cmd_doc(message: Message):
    """
    Handler for the `/documentation` command
    """

    await message.reply_document(
        document=FSInputFile(path="assets/tech_doc.docx", filename="техническая документация.docx")
    )


@dp.message(Command("presentation"))
async def cmd_presentation(message: Message):
    """
    Handler for the `/presentation` command
    """

    await message.reply_document(
        document=FSInputFile(path="assets/pressetation.pptx", filename="презентация.pptx")
    )


async def main() -> None:
    """
    Main function to start the bot
    """

    logging.info("Starting bot")

    dp.message.filter(F.chat.type == ChatType.PRIVATE)
    dp.callback_query.filter(F.message.chat.type == ChatType.PRIVATE)

    await set_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
