from config import TELEGRAM_BOT_TOKEN
import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from handlers.tools import calc

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(calc.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())
