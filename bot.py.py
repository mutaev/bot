import requests
import datetime
import logging
from config import TOKEN , open_weather_token
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import random

#TOKEN = "1858888495:AAGsdLWQ1lZgVxRSW2pza6AwC7l0OGwmws4"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ассаламу Алейкум {0.first_name}'.format(message.from_user),reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    #await bot.send_message(message.from_user.id, message.text)
    if message.text == '🔸 Рандомное число':
        await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(1000, 9999)))

    elif message.text == '⬅️ Главное меню':
        await bot.send_message(message.from_user.id, '⬅️ Главное меню', reply_markup=nav.mainMenu)

    elif message.text == '➡️ Другое':
        await bot.send_message(message.from_user.id, '➡️ Другое', reply_markup=nav.otherMenu)

    elif message.text == '📓 Информация':
        await bot.send_message(message.from_user.id, ' Я Зубенко Михаил Петрович 🎩 \n💻 DISCORD разработчика "Хэнкок#6413"')


    elif message.text == '📈 Курсы валют':
        await bot.send_message(message.from_user.id, 'Курсы валют')

    elif message.text == '⌚ Время намаза':
        await bot.send_message(message.from_user.id, 'Данная функция в разработке⚙️')

    else:
        await message.reply('Неизвестная команда')















if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


















