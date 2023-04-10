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

    Wait message with command start to start telegram bot and send information about it's functionality.

    :param message: message from user with command /start
    :return: information about functionality of the TelegramBot and useful information about TelegramBot

    """

    # Wait a messege /start from user
    await message.reply("Hi, I'm a telegram bot that can give you current weather in such city what would you like)\n\n"
                        "Send /help - get some information about commands and functionality of telegram bot\n"
                        )

@dp.message_handler(commands=["help"])
async def command_list(message: types.Message):
    """

    Send message with common comands of telegram bot.

    :param message: message from user with command /help
    :return: information about common commands in TelegramBot

    """
    await message.reply("Input the name of city in which you want to now what weather is in it.")


@dp.message_handler()
async def getWeather(message: types.Message):
    """

    Take the name of the city from user and then get request to openweather api to get current weather in the user's
    city. Then send data to user.

    :param message: message from user with name of the city
    :return: current weather in the city, which was entered by user and suggest to get more exetended forcast
    for 5 days in the city

    """
    try:
        await image_download(message)

        # Get request to openweather api
        result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OWM}&units=metric')
        # Get data and write it into json
        data = result.json()

        # Get data
        city = data["name"]
        country = data["sys"]["country"]
        humadiry = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        temp = data["main"]["temp"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        weather = data["weather"][0]["description"]

        # Check emoji in emoji code and if it is send it
        if weather in emodji_code:
            wd = emodji_code[weather]
        else:
            wd = "Undentified weather"

        wind = data["wind"]["speed"]

        # Convert length of the day into YY-MM-DD hour:minute:seconds format
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        # Send converted data to user
        await bot.send_message(message.from_user.id, f'The weather in {city}({country}) is {wd}\nTemperature: {temp} °C\nPressure: {pressure} mm Hg\n'
              f'The wind: {wind} km/h\nHumadiry: {humadiry}%\nSunset: {sunset_timestamp}\nSunrise: {sunrise_timestamp}\n'
              f'Length of the day: {length_of_the_day} '
                            )

        # Create keyboard and send it to user
        keyboard_to_choice = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('Yes', callback_data=f'{message.text}'),
                    InlineKeyboardButton('No', callback_data='no')
                ]
            ]
        )

        # Wait a choice from user to send him forcast weather or not
        await bot.send_message(message.from_user.id, f'Do you want to see some 5 days forcast in {message.text}?',
                               reply_markup=keyboard_to_choice)


        # If choice Yes, start forcast function
        @dp.callback_query_handler(lambda call: True, text=f'{message.text}')
        async def weather_forcast_5_days(call: CallbackQuery):
            await forcast(message)

        # If not, wait another name of the city
        @dp.callback_query_handler(text='no')
        async def no_weather_5_days_forcast(call: CallbackQuery):
            await call.message.answer('Okay, set another name of the city.')


    # If the name of the city wrong, raise an exception
    except Exception as e:
        print(e)
        await bot.send_message(message.from_user.id, "Check the name of city")


async def forcast(message: types.Message):
    """

    Get reauest to openweather api to get 3 hour 5 days forcast in the current city.

    :param message: message from user with name of the city
    :return: 5 days forcast in the city with at intervals for 3 hours, and return diagram with temperature forcast
    at interval for 3 hours for 5 days

    """
    try:

        #Get request to openweather api
        result = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={message.text}&limit=5&appid={OWM}')
        data = result.json()

        # Get coordinates of the cty
        lat = data[0]["lat"]
        lon = data[0]["lon"]

        # Post coordinates into request
        r = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OWM}&units=metric')

        # Get request data
        res = r.json()

        # Get forcast for 5 days every 3 hours
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

                    # Send to user message with forcast
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

        # Start function to build a diagram of temperature changes
        diagram(message)

        #Open image with diagram
        img = open('diagram.png', 'rb')
        # Send image to user
        await bot.send_photo(message.chat.id, img)

        # Send to user the link to wiki with his city to get more information about it
        await bot.send_message(message.from_user.id, 'If you want to know more about the city, here is a link')
        await bot.send_message(message.from_user.id, f'https://en.wikipedia.org/wiki/{message.text.title()}')


    except Exception as e:
        await bot.send_message(message.from_user.id, f"Check the name of city {e}")

    # Clear temperature and time lists
    temperature.clear()
    times.clear()


def diagram(message):
    """

    This function get data from forcast func and post it to build diagram of temperature changes.

    :param message: message from user
    :return: diagram with temperature at intervals for 3 hours for 5 days

    """

    # Set coordinates
    x = np.arange(0, len(temperature))
    y = temperature

    # Create figure
    fig, ax = plt.subplots()

    # Set width of colomns
    ax.bar(x, y, width=0.77)

    # Set background and colomns colors, and width and height of figure
    ax.set_facecolor('seashell')
    fig.set_figwidth(20)  # Figure width
    fig.set_figheight(10)  # Figure height
    fig.set_facecolor('floralwhite')

    # Set labels
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

    # Save figure to diagram.png
    plt.savefig('diagram.png', dpi=300)


async def image_download(message: types.Message):
    """

    This function get request and download an image of the city, wwhich was entered by user.

    :param message: the name of the city entered by user
    :return: image of the cuty

    """

    # Get a request to www.google.com
    res = requests.get(
        f'https://www.google.by/search?q={message.text}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiJ1K7Y8OX9AhUUgosKHS4NBm4Q_'
        'AUoAXoECAEQAw&biw=1470&bih=839&dpr=2')

    img = []

    # Take tegs with images
    soup = BeautifulSoup(res.text, 'html.parser')
    images = soup.find_all('img')

    for image in images:
        img.append(image['src'])

    for i in img:
        if re.search('gif', i):
            img.remove(i)

    # Set path to the image
    path = 'city_image.png'
    # Save request data in bites to the path
    if len(img) != 0:
        response = requests.get(img[0])
        print(response.status_code)
        if response.status_code == 200:
            with open(path, 'wb') as f:
                f.write(response.content)

    # Read path in bites and send image to user
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