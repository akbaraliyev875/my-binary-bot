import telebot
from flask import Flask
import threading
import os

# 1. Botingiz tokini (Siz bergan token)
TOKEN = "7718903337:AAH0pP34uW2e3m1vO-6r3D3M3gX6N3M3"
bot = telebot.TeleBot(TOKEN)

# 2. Render uchun kichik veb-server (uyg'otgich)
app = Flask('')

@app.route('/')
def home():
    return "Bot yoniq va ishlayapti, akajon!"

def run():
    # Render portni avtomatik beradi
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# 3. Bot buyruqlari (Sizning asosiy kodingiz)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Botingiz Render'da muvaffaqiyatli ishlayapti, akajon! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Bu yerga o'zingizning Binary (sonlar tizimi) mantiqingizni qo'shishingiz mumkin
    bot.reply_to(message, f"Siz yozdingiz: {message.text}")

# 4. Botni yurgizish
if __name__ == "__main__":
    keep_alive() # Serverni yoqamiz (Render o'chirmasligi uchun)
    print("Bot xabarlarni kutmoqda...")
    bot.polling(none_stop=True)
