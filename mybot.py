import telebot
from telebot import types

bot = telebot.TeleBot("2085972468:AAGeOVKzNEwAbFr-rwiNsEQYujs8eT8Ngbs", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ism = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tugma1 = "👨‍💻Bizning Kurslar"
    tugma2 = "👥Biz Haqimizda"
    tugma3 = "🏢Biznig Manzil"
    markup.add(tugma2, tugma1, tugma3)

    text = f"Assalomu aleykum {ism}.\nO'quv markazimiznig rasmiy botiga xush kelibsiz"

    bot.reply_to(message, text, reply_markup=markup)

@bot.message_handler(content_types=["text"])
def send_answer(message):
    if message.text == "👨‍💻Bizning Kurslar":
        
        inlinekm = types.InlineKeyboardMarkup()
        in1 = types.InlineKeyboardButton("Python", callback_data="python")
        in2 = types.InlineKeyboardButton("Java", callback_data="java")
        in3 = types.InlineKeyboardButton("C++", callback_data="c++")
        in4 = types.InlineKeyboardButton("JavaScript", callback_data="javascript")
        inlinekm.row(in1,in2).row(in3, in4)

        bot.send_message(message.from_user.id,"<b>Bizda quyidagi kurslar mavjud👇:</b>", reply_markup=inlinekm, parse_mode='html')

    elif message.text == "👥Biz Haqimizda":
        pass

    elif message.text == "🏢Biznig Manzil":
        pass


@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    if call.data == "python":
        bot.answer_callback_query(call.id, "Python Kursimiz haqida")
        bot.send_message(call.message.chat.id, "Python kursi haqida ma'lumot")








bot.infinity_polling()    