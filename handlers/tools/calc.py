from aiogram import Router
from aiogram.types import Message
from main import bot
router = Router()


@router.message(content_types="photo")
async def get_xp_for_new_level_by_photo(message: Message):
    await bot.download(file=message.photo[-1].file_id, destination=r"D:\dev\PocketCombatsTelegramBot\123.png")

