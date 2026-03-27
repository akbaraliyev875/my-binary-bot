import telebot
from flask import Flask
import threading
import os
import time

# 1. Botingiz tokini (Siz bergan token)
TOKEN = "7718903337:AAH0pP34uW2e3m1vO-6r3D3M3gX6N3M3"
bot = telebot.TeleBot(TOKEN)

# 2. Render o'chirib qo'ymasligi uchun Flask server
app = Flask('')

@app.route('/')
def home():
    return "Bot yoniq va ishlayapti!"

def run():
    # Render portni avtomatik beradi
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# 3. Bot buyruqlari
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Botingiz Render'da muvaffaqiyatli ishga tushdi, akajon! 🚀\n\nIkkilik (Binary) sonlarni yuboring, men ularni hisoblab beraman.")

# Bu yerga binary mantiqingizni yoki echo-ni qo'shamiz
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    bot.reply_to(message, f"Siz yuborgan xabar: {text}\n\nBot hozirda xabarlarni qabul qilmoqda!")

# 4. Botni xatolarsiz yurgizish (Infinity Polling)
if __name__ == "__main__":
    keep_alive() # Serverni yoqamiz
    print("Render server ishga tushdi...")
    
    # Botni to'xtovsiz ishlashi uchun cheksiz sikl
    while True:
        try:
            print("Bot xabarlarni kutmoqda...")
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print(f"Xato yuz berdi: {e}")
            time.sleep(5) # Xato bo'lsa 5 soniya kutib qayta urinadi
