import asyncio

from aiogram import Router
from aiogram.types import Message
from main import bot
from modules.get_xp_for_next_lvl.get_xp import Action_xp_page
router = Router()


@router.message(content_types="photo")
async def get_xp_for_new_level_by_photo(message: Message):
    await bot.download(file=message.photo[-1].file_id, destination=r"D:\dev\PocketCombatsTelegramBot\123.png")
    loop = asyncio.get_running_loop()
    try:
        now, need = await loop.run_in_executor(None, lambda: get_xp(r"D:\dev\PocketCombatsTelegramBot\123.png"))
        await message.answer(f"До нового уровня вам нужно {need - now} опыта!")
    except Exception:
        await message.answer(f"Такой формат не поддеживается, сооббщение разработчик отправленно!")



def get_xp(path):
    xp_page = Action_xp_page()
    now, need = xp_page.get_xp(path)
    return now, need

