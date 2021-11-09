from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Главное меню"]
    keyboard.add(*buttons)
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=keyboard)


####################################################################################

@dp.message_handler(Text(equals="Главное меню"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Первая кнопка", "Вторая кнопка"]
    keyboard.add(*buttons)
    await message.reply("Выбрать режим", reply_markup=keyboard)


@dp.message_handler(Text(equals="Первая кнопка"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["+ кнопка", "- кнопка", "Главное меню"]
    keyboard.add(*buttons)
    await message.reply("Выбрать режим", reply_markup=keyboard)


@dp.message_handler(Text(equals="+ кнопка"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Сохранить", "Отмена", "Главное меню"]
    keyboard.add(*buttons)

    @dp.message_handler()
    async def echo_message(msg: types.Message):
        print(msg.text)


    await message.reply("Укажите названия канала ", reply_markup=keyboard)


@dp.message_handler(Text(equals="Сохранить"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Главное меню"]
    keyboard.add(*buttons)
    print('NAME CHANNEL: ')
    await message.reply("Канал добавлен", reply_markup=keyboard)


####################################################################################
@dp.message_handler(Text(equals="Вторая кнопка"))
async def with_puree(message: types.Message):
    await message.reply("Выбрана Вторую кнопку!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     print(msg.text)
#     await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
