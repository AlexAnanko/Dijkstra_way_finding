import requests
import datetime
from .config import API_TOKEN, OWM
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from django.core.management.base import BaseCommand
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import re
from .emodji_code import emodji_code

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

temperature = []
dates = []
times = []

@dp.message_handler(commands=["start"])
async def command_list(message: types.Message):
    """

    :param message: message from user with command /start
    :return: information about functionality of the TelegramBot and useful information about TelegramBot

    """

    await message.reply("Hi, I'm a telegram bot that can give you current weather in such city what would you like)\n\n"
                        "Send /help - get some information about commands and functionality of telegram bot\n"
                        )

@dp.message_handler(commands=["help"])
async def command_list(message: types.Message):
    """

    :param message: message from user with command /help
    :return: information about common commands in TelegramBot

    """
    await message.reply("Input the name of city in which you want to now what weather is in it.")


@dp.message_handler()
async def getWeather(message: types.Message):
    """

    :param message: message from user with name of the city
    :return: current weather in the city, which was entered by user and suggest to get more exetended forcast
    for 5 days in the city

    """
    try:
        await image_download(message)

        result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OWM}&units=metric')
        data = result.json()

        city = data["name"]
        country = data["sys"]["country"]
        humadiry = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        temp = data["main"]["temp"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        weather = data["weather"][0]["description"]

        if weather in emodji_code:
            wd = emodji_code[weather]
        else:
            wd = "Undentified weather"

        wind = data["wind"]["speed"]
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await bot.send_message(message.from_user.id, f'The weather in {city}({country}) is {wd}\nTemperature: {temp} °C\nPressure: {pressure} mm Hg\n'
              f'The wind: {wind} km/h\nHumadiry: {humadiry}%\nSunset: {sunset_timestamp}\nSunrise: {sunrise_timestamp}\n'
              f'Length of the day: {length_of_the_day} '
                            )

        keyboard_to_choice = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Yes', callback_data=f'{message.text}'),
                    InlineKeyboardButton('No', callback_data='no')
                ]
            ]
        )

        await bot.send_message(message.from_user.id, f'Do you want to see some 5 days forcast in {message.text}?',
                               reply_markup=keyboard_to_choice)


        @dp.callback_query_handler(lambda call: True, text=f'{message.text}')
        async def weather_forcast_5_days(call: CallbackQuery):
            await forcast(message)

        @dp.callback_query_handler(text='no')
        async def no_weather_5_days_forcast(call: CallbackQuery):
            await call.message.answer('Okay, set another name of the city.')


    except Exception as e:
        print(e)
        await bot.send_message(message.from_user.id, "Check the name of city")


async def forcast(message: types.Message):
    """

    :param message: message from user with name of the city
    :return: 5 days forcast in the city with at intervals for 3 hours, and return diagram with temperature forcast
    at interval for 3 hours for 5 days

    """
    try:


        result = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={message.text}&limit=5&appid={OWM}')
        data = result.json()
        # pprint(data)

        lat = data[0]["lat"]
        lon = data[0]["lon"]

        r = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OWM}&units=metric')

        res = r.json()
        # pprint(res)

        for i in range(40):
            current_city = res["city"]["name"]
            date = datetime.datetime.fromtimestamp(res["list"][i]["dt"])
            date_text = res["list"][i]["dt_txt"]
            time_loc = date_text[8:-1]
            feels_like = res["list"][i]["main"]["feels_like"]
            humidity = res["list"][i]["main"]["humidity"]
            pressure = res["list"][i]["main"]["pressure"]
            temp = res["list"][i]["main"]["temp"]
            temp_max = res["list"][i]["main"]["temp_max"]
            temp_min = res["list"][i]["main"]["temp_min"]
            wind = res["list"][i]["wind"]["speed"]
            weather = res["list"][i]["weather"][0]["description"]
            temperature.append(temp)
            dates.append(date)
            times.append(time_loc)
            if not i % 12 != 0:
                if i < 3:

                    if weather in emodji_code:
                        wd = emodji_code[weather]
                    else:
                        wd = "Undentified weather"

                    await bot.send_message(message.from_user.id, f'Weather forcast in {current_city} for {date}\nWeather: {weather}, {wd}'
                          f'Feels like: {feels_like}\nHumidity: {humidity}\n'
                          f'Pressure: {pressure}\nTemperature: {temp}\nMaximum temperature: {temp_max}\nMinimum temperature: {temp_min}\n'
                          f'Wind: {wind}\n')
                else:
                    if weather in emodji_code:
                        wd = emodji_code[weather]
                    else:
                        wd = "Undentified weather"

                    await bot.send_message(message.from_user.id, f'Weather forcast in {current_city} for {date}\nWeather: {weather} {wd}'
                          f'Feels like: {feels_like}\nHumidity: {humidity}\n'
                          f'Pressure: {pressure}\nTemperature: {temp}\n'
                          f'Wind: {wind}\n')

        diagram(message)

        img = open('diagram.png', 'rb')
        await bot.send_photo(message.chat.id, img)

        await bot.send_message(message.from_user.id, 'If you want to know more about the city, here is a link')
        await bot.send_message(message.from_user.id, f'https://en.wikipedia.org/wiki/{message.text.title()}')


    except Exception as e:
        await bot.send_message(message.from_user.id, f"Check the name of city {e}")

    temperature.clear()
    times.clear()


def diagram(message):
    """

    :param message: message from user
    :return: diagram with temperature at intervals for 3 hours for 5 days
    """
    x = np.arange(0, len(temperature))
    y = temperature

    fig, ax = plt.subplots()

    ax.bar(x, y, width=0.77)

    ax.set_facecolor('seashell')
    fig.set_figwidth(20)  # ширина Figure
    fig.set_figheight(10)  # высота Figure
    fig.set_facecolor('floralwhite')

    plt.xlabel('Time and date', fontsize=14)
    plt.ylabel('Temperature, °C', fontsize=14)
    plt.title(f'Weather in {message.text}', fontsize=16)
    plt.xticks(x, times, rotation=45, fontsize=10)
    plt.legend(['Temperature'], fontsize=10)

    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = 5
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,  # Use `label` as label
            (x_value, y_value),  # Place label at end of the bar
            xytext=(0, space),  # Vertically shift label by `space`
            textcoords="offset points",  # Interpret `xytext` as offset in points
            ha='center',  # Horizontally center label
            va=va)  # Vertically align label differently for
        # positive and negative values.

    plt.savefig('diagram.png', dpi=300)


async def image_download(message: types.Message):
    res = requests.get(
        f'https://www.google.by/search?q={message.text}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiJ1K7Y8OX9AhUUgosKHS4NBm4Q_'
        'AUoAXoECAEQAw&biw=1470&bih=839&dpr=2')

    img = []
    soup = BeautifulSoup(res.text, 'html.parser')
    images = soup.find_all('img')

    for image in images:
        img.append(image['src'])

    for i in img:
        if re.search('gif', i):
            img.remove(i)

    path = 'city_image.png'
    if len(img) != 0:
        response = requests.get(img[0])
        print(response.status_code)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)

    photo = open('city_image.png', 'rb')
    await bot.send_photo(message.chat.id, photo)

class Command(BaseCommand):
    help = 'Test TG Bot'

    def handle(self, *args, **options):
        executor.start_polling(dp)

if __name__ == "__main__":
    try:
        executor.start_polling(dp, loop=None, skip_updates=True, reset_webhook=True, on_startup=None, on_shutdown=None,
                               timeout=20, )
    except Exception as e:
        print(datetime.datetime, e)