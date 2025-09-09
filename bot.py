import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

# Вставь сюда токен своего бота от @BotFather
BOT_TOKEN = "8344183587:AAFElP7UxXJ8WSKvzqHmf-wvz9HOs_1auMA"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# --- Ссылки на каналы по городам ---
CITY_CHANNELS = {
    "Москва": "https://t.me/amorefloraMoscow",
    "Санкт-Петербург": "https://t.me/amorefloraSanktPetersburg",
    "Казань": "https://t.me/amorefloraKazan",
    "Екатеринбург": "https://t.me/amorefloraEkaterenburg"
}

# --- Клавиатуры ---
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("🌸 Выбрать город"))

cities_menu = ReplyKeyboardMarkup(resize_keyboard=True)
for city in CITY_CHANNELS.keys():
    cities_menu.add(city)
cities_menu.add("🔙 Назад")

# --- Обработчики ---
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    text = (
        "🌸 Добро пожаловать в *FlowerTime*!\n\n"
        "Мы — команда профессионалов в сфере доставки цветов 💐. Уже более *6 лет* мы делаем людей счастливее, "
        "создавая красоту в каждом букете.\n\n"
        "Почему выбирают нас?\n"
        "✨ Собственные плантации рядом с каждым городом — цветы всегда свежие, как только с грядки.\n"
        "💰 Самые низкие цены, потому что мы работаем напрямую, без посредников.\n"
        "🚚 Быстрая доставка — от момента заказа до счастливого получателя проходит минимум времени.\n"
        "🎁 Для нас каждый заказ — это маленький праздник, и мы делаем его особенным!\n\n"
        "Выберите город, чтобы перейти в каталог и подобрать идеальный букет:"
    )
    await message.answer(text, reply_markup=main_menu, parse_mode="Markdown")

@dp.message_handler(lambda message: message.text == "🌸 Выбрать город")
async def choose_city(message: types.Message):
    await message.answer("🏙 Пожалуйста, выберите ваш город:", reply_markup=cities_menu)

@dp.message_handler(lambda message: message.text in CITY_CHANNELS.keys())
async def send_channel(message: types.Message):
    city = message.text
    channel_link = CITY_CHANNELS[city]
    await message.answer(
        f"💐 Отличный выбор! Для города *{city}* у нас есть отдельный каталог 🌷\n\n"
        f"Перейдите по ссылке и подберите свой букет: {channel_link}",
        parse_mode="Markdown"
    )
    # --- Добавляем акцию ---
    await message.answer(
        "🔥 Специальное предложение!\n\n"
        "Закажите *2 букета* и получите второй со скидкой **-30%** 🎁\n"
        "Успейте порадовать близких прямо сегодня ❤️",
        parse_mode="Markdown"
    )

@dp.message_handler(lambda message: message.text == "🔙 Назад")
async def back(message: types.Message):
    await message.answer("⬅️ Возвращаемся в главное меню:", reply_markup=main_menu)

# --- Запуск ---
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)








 