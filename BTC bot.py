import telebot
import requests

# توکن ربات شما
TOKEN = "7645961434:AAHz2Foq7QzRdMUVlU_pg9n3xqsy42CDS4M"
bot = telebot.TeleBot(TOKEN)

# گرفتن قیمت بیت‌کوین از API
def get_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    data = response.json()
    price = data["bpi"]["USD"]["rate"]
    return f"قیمت بیت‌کوین: ${price}"

# پاسخ به /start
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "سلام! برای دریافت قیمت بیت‌کوین، دستور /btc رو بفرست.")

# پاسخ به /btc
@bot.message_handler(commands=["btc"])
def btc_price(message):
    price = get_btc_price()
    bot.reply_to(message, price)

print("ربات روشنه...")
bot.polling()
