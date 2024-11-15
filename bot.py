from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import asyncio, logging
from config import token
import random
bot = Bot(token=token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

random_number = random.randint(1, 3)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Я загадал число от 1 до 3 Угадайте его")

@dp.message(F.text == "1")
async def ugadaniy_chislo(message: Message):
    if random_number == 3:
        await message.reply("Правильно вы отгадали")
    else:
        await message.reply("Неправильно попробуйте снова")

@dp.message(F.text == "2")
async def ugadaniy_chislo(message: Message):
    if random_number == 2:
        await message.reply("Правильно вы отгадали")
    else:
        await message.reply("Неправильно попробуйте снова")

@dp.message(F.text == "3")
async def ugadaniy_chislo(message: Message):
    if random_number == 3:
        await message.reply("Правильно вы отгадали")
    else:
        await message.reply("Неправильно попробуйте снова")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



# message.reply("Правильно вы отгадали")




















# @dp.message(Command('help'))
# async def help(message: Message):
#     await message.reply('Чем могу помочь')

# @dp.message(Command('contact'))
# async def contact(message: Message):
#     await message.answer_contact(last_name = "Biloliddin", first_name = 'Botirov', phone_number = "+996551977778")

# @dp.message(Command('location'))
# async def location(message: Message):
#     await message.answer_location(latitude=40.50950344111354, longitude= 72.51272575804961)

# @dp.message(Command('photo'))
# async def photo(message: Message):
#     await message.answer_photo(photo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCTT8o6deC4Pj7sYfFG033BFQ5qoaHXxy_Yg&s")

# @dp.message(F.text == "backend")
# async def hello(message: Message):
#     await message.reply("Backend-разработка — это серверная часть веб-приложения или сайта, которая отвечает за обработку логики, взаимодействие с базой данных, аутентификацию, авторизацию и многое другое.")

# @dp.message(F.text == "frontend")
# async def hello(message: Message):
#     await message.reply("Фронтенд — это часть веб-разработки, которая отвечает за внешний вид сайта и взаимодействие с пользователем. Это то, что пользователь видит и с чем он взаимодействует на сайте. В отличие от бэкенда, фронтенд разрабатывается с помощью HTML, CSS и JavaScript.")

# @dp.message(F.text == "ux/ui")
# async def hello(message: Message):
#     await message.reply("Давай поговорим про UX/UI. Что именно тебя интересует? Это может быть:Советы по дизайну интерфейсов: Цвета, типографика, расположение элементов.Прототипирование и инструменты: Figma, Adobe XD или другие программы.Оптимизация пользовательского опыта (UX): Исследование пользовательских сценариев, юзабилити-тесты.")

# @dp.message(F.text == "about")
# async def hello(message: Message):
#     await message.reply("Я учусь в направлении Бекенд мне 17 лет ")