import telebot

from telebot import types



# Sizning tokeningiz

TOKEN = '8399170869:AAF0077BXYDH6EyHqQ7nm_Ah2NsaJtTZYPU'

bot = telebot.TeleBot(TOKEN)



# Foydalanuvchi holatini saqlash

user_status = {}



def main_buttons():

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    btn1 = types.KeyboardButton("⬅️ 2-likdan ➡️ 10-likka")

    btn2 = types.KeyboardButton("⬅️ 10-likdan ➡️ 2-likka")

    btn3 = types.KeyboardButton("🧮 Kalkulyator")

    btn4 = types.KeyboardButton("📞 Biz bilan bog'lanish")

    markup.add(btn1, btn2, btn3, btn4)

    return markup



@bot.message_handler(commands=['start'])

def start(message):

    bot.send_message(message.chat.id, "Assalomu alaykum! Kerakli bo'limni tanlang:",

                     reply_markup=main_buttons())



@bot.message_handler(func=lambda message: True)

def handle_text(message):

    chat_id = message.chat.id

    text = message.text



    if text == "⬅️ 2-likdan ➡️ 10-likka":

        user_status[chat_id] = "2to10"

        bot.send_message(chat_id, "Ikkilik sonni yuboring (faqat 0 va 1):")



    elif text == "⬅️ 10-likdan ➡️ 2-likka":

        user_status[chat_id] = "10to2"

        bot.send_message(chat_id, "O'nlik sonni yuboring (masalan: 25):")



    elif text == "🧮 Kalkulyator":

        user_status[chat_id] = "calc"

        bot.send_message(chat_id, "Matematik misolni yuboring (masalan: 10+5*2):")



    elif text == "📞 Biz bilan bog'lanish":

        contact_info = (

            "<b>👨‍💻 Admin bilan bog'lanish:</b>\n\n"

            "🔹 <b>Telegram:</b> <a href='https://t.me/FromGuliston'>FromGuliston</a>\n"

            "🔹 <b>Instagram:</b> <a href='https://www.instagram.com/sahiy.aka/'>sahiy.aka</a>\n"

            "🔹 <b>Telefon:</b> +998 55 555 55 55\n\n"

            "Savollaringiz bo'lsa, bemalol murojaat qiling!"

        )

        bot.send_message(chat_id, contact_info, parse_mode='HTML', disable_web_page_preview=False)



    else:

        status = user_status.get(chat_id)



        if status == "2to10":

            try:

                res = int(text, 2)

                bot.send_message(chat_id, f"✅ Natija (O'nlikda): {res}")

            except:

                bot.send_message(chat_id, "Xato! Faqat 0 va 1 yuboring.")



        elif status == "10to2":

            try:

                res = bin(int(text))[2:]

                bot.send_message(chat_id, f"✅ Natija (Ikkilikda): {res}")

            except:

                bot.send_message(chat_id, "Xato! Faqat butun son yuboring.")



        elif status == "calc":

            try:

                # Faqat xavfsiz belgilarni qoldirish

                allowed_chars = "0123456789+-*/. "

                if all(c in allowed_chars for c in text):

                    res = eval(text.replace(' ', ''))

                    bot.send_message(chat_id, f"✅ Natija: {res}")

                else:

                    bot.send_message(chat_id, "Faqat raqamlar va amallar (+, -, *, /)!")

            except:

                bot.send_message(chat_id, "Misolda xato bor, qayta tekshiring.")



        else:

            bot.send_message(chat_id, "Iltimos, tugmalardan birini tanlang!", reply_markup=main_buttons())



print("Botingiz yangi bo'lim bilan ishga tushdi, akajon!")

bot.polling(none_stop=True)
