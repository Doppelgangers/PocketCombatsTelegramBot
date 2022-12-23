import asyncio

from aiogram import Router, Bot
from aiogram.types import Message

from modules.get_xp_for_next_lvl.get_xp import Action_xp_page
router = Router()


@router.message(content_types="photo")
async def get_xp_for_new_level_by_photo(message: Message, bot: Bot):
    await bot.download(file=message.photo[-1].file_id, destination=r"D:\dev\PocketCombatsTelegramBot\123.png")
    loop = asyncio.get_running_loop()
    try:
        now, need = await loop.run_in_executor(None, lambda: get_xp(r"D:\dev\PocketCombatsTelegramBot\123.png"))
        next_lvl = need - now
        await message.answer(f"До нового уровня вам нужно {format_lvl(next_lvl)} опыта!")
    except Exception as e:
        print(e)
        await message.answer(f"Такой формат не поддеживается, сооббщение разработчик отправленно!")


def get_xp(path):
    xp_page = Action_xp_page()
    now, need = xp_page.get_xp(path)
    return now, need


def format_lvl(num: int, sep: str = " ") -> str:
    """
    :param num: Любое целое число
    :param sep: Разделитель между числами
    :return str: Возвращает отформатированное число в виде строи с отступами. 1234 -> '1 234'
    """
    num = str(num)

    if need_add := num.__len__() % 3 != 0:
        num = need_add*" " + num

    chunks = [num[i:i+3].strip() for i in range(0, num.__len__(), 3)]
    return sep.join(chunks)

lst = [1,1,1,1]

lst2 = [ el*2  for el in lst  ]

lst2 = []
for el in lst:
    lst2.append(el * 2)