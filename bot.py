import telebot
from telebot import types
from sqlalchemy import Integer,MetaData,create_engine,Column,String, Table, Integer, update, delete

bot = telebot.TeleBot("2083500114:AAEr-mLLyXt_FOPQd7vAVJ6IY_wI_QXG7OI", parse_mode=None)

engine = create_engine('sqlite:///base.db', echo = True)
meta =MetaData()

users = Table(
    'users',meta,
    Column('id',Integer,primary_key = True),
    Column('name',String),
    Column('lastname',String),
    Column('username',String),
    Column('user_id',Integer),

)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ism = message.from_user.first_name
    familya = message.from_user.last_name
    user_id=message.from_user.id
    username = message.from_user.username

    meta.create_all(engine)
    ins = users.insert()
    ins = users.insert().values(name = "ism", lastname = "familya", user_id = message.from_user.id, username = 'sasasas' )
    conn = engine.connect()
    result = conn.execute(ins)


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('delete')
    markup.add('update')
    reply_text= 'Assalomu Aleykum '+ism
    bot.send_message(user_id ,reply_text,reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text_handler(message):
    if message.text == "delete":
        stmt = (
            delete(users).
            where(users.c.user_id == message.from_user.id)
        )

        conn = engine.connect()
        result = conn.execute(stmt) 

    elif message.text == 'update':
        stmt = (
            update(users).
            where(users.c.user_id == message.from_user.id).values(lastname = "updateboldi")
        )

        conn = engine.connect()
        result = conn.execute(stmt) 

bot.infinity_polling()    