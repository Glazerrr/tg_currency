import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from currency import valutes_list
import os
from  curparser import mainfunc, dateformat
# Загрузка переменных из .env


# Получение значения токена
API_TOKEN = os.getenv("TOKEN")



logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот выдающий актуальный курс. Выбери интересующие тебя валюты")
    await send_currency_selection(message)


async def send_currency_selection(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    print(valutes_list(), valutes_list()[3])    
    currencies = ['Австралийский доллар', 'Азербайджанский манат', 'Фунт стерлингов Соединенного королевства', 'Армянских драмов', 'Белорусский рубль', 'Болгарский лев', 'Бразильский реал', 'Венгерских форинтов', 'Вьетнамских донгов', 'Гонконгский доллар', 'Грузинский лари', 'Датская крона', 'Дирхам ОАЭ', 'Доллар США', 'Евро', 'Египетских фунтов', 'Индийских рупий', 'Индонезийских рупий', 'Казахстанских тенге', 'Канадский доллар', 'Катарский риал', 'Киргизских сомов', 'Китайский юань', 'Молдавских леев', 'Новозеландский доллар', 'Норвежских крон', 'Польский злотый', 'Румынский лей', 'Сингапурский доллар', 'Таджикских сомони', 'Таиландских батов', 'Турецких лир', 'Новый туркменский манат', 'Узбекских сумов', 'Украинских гривен', 'Чешских крон', 'Шведских крон', 'Швейцарский франк', 'Сербских динаров', 'Южноафриканских рэндов', 'Вон Республики Корея', 'Японских иен']
    for currency in currencies:
        callback_data = f'choose_currency:{currency}'
        keyboard.add(types.InlineKeyboardButton(text=currency, callback_data=callback_data))
    await message.answer("Выберите валюту, которую вы хотите видеть в ежедневном обновлении курса:", reply_markup=keyboard)

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.reply(message.text)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
