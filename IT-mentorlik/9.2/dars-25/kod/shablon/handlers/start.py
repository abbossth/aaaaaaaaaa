from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


def menyu():
    kb = ReplyKeyboardBuilder()
    for t in ("📋 Funksiya 1", "⭐ Funksiya 2", "ℹ️ Yordam"):
        kb.button(text=t)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(f"Salom, {message.from_user.first_name}! 👋\nBot nima qiladi: ...", reply_markup=menyu())


@router.message(Command("help"))
async def help_cmd(message: Message) -> None:
    await message.answer("Buyruqlar: /start, /help")
