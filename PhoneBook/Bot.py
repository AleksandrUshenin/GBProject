
from cgitb import text
from main import Program

import telebot
from telebot import types

name = ''
patronymic = ''
surname = ''
number = ''
textStr = ''

bot = telebot.TeleBot("5228215323:AAEKbGo5nILd9gYYSIQTbd1EYQq441G7PO8", parse_mode=None)

pro =  Program(bot)
pro.Run()

me = bot.get_me()

@bot.message_handler(commands = 'menu')
def send_welcome(message):
    bot.reply_to(message, pro.Run())

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    #print(message)
#	bot.send_message(chat_id = message.chat.id , text = pro.Do_Commands(message, message.text))

#@bot.message_handler(content_types=['text'])
#def get_text_messages(message):
    #if message.text == "Привет":
    #    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    #elif message.text == "/help":
    #    bot.send_message(message.from_user.id, "Напиши привет")
    #else:
    #    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")  

@bot.message_handler(content_types=['text'])
def Add_User(message):
    print('message.text', message.text)
    if message.text == 'add':
        bot.send_message(message.from_user.id, "Введите имя: ")
        bot.register_next_step_handler(message, Get_Name)
    elif message.text == 'print':
        bot.send_message(message.from_user.id, pro.Do_Commands('2', ''))
    elif message.text == 'delete':
        bot.send_message(message.from_user.id, "Введите id для удоления: ")
        bot.register_next_step_handler(message, Delete)
    elif message.text == 'serid':
        bot.send_message(message.from_user.id, "Введите id: ")
        bot.register_next_step_handler(message, Searchid)
    elif message.text == 'ser':
        bot.send_message(message.from_user.id, "Введите фамилию: ")
        bot.register_next_step_handler(message, Search)
    elif message.text == 'load':
        bot.send_message(message.from_user.id, "Введите способ для загрузки:\n1 - через json\n2 - через html")
        bot.register_next_step_handler(message, Load)
    elif message.text == 'save':
        bot.send_message(message.from_user.id, "Введите способ для сохранения:\n1 - через json\n2 - через html")
        bot.register_next_step_handler(message, Save)

def Get_Name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Введите отчество: ")
    bot.register_next_step_handler(message, Get_Patronymic)

def Get_Patronymic(message):
    global patronymic
    patronymic = message.text
    bot.send_message(message.from_user.id, "Введите фамилию: ")
    bot.register_next_step_handler(message, Get_Surname)
    
def Get_Surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Введите номер: ")
    bot.register_next_step_handler(message, Get_Number)

def Get_Number(message):
    global number
    global textStr
    number = message.text
    textStr = f'{name} {patronymic} {surname} {number}'
    keyboard = Buttons(message)
    bot.send_message(message.from_user.id, f'User = {textStr}', reply_markup = keyboard)

def Buttons(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    return keyboard

def Delete(message):
    global id
    id = int(message.text)
    bot.send_message(message.from_user.id, pro.Do_Commands('3', id))

def Searchid(message):
    id = int(message.text)
    bot.send_message(message.from_user.id, pro.Do_Commands('4', id))

def Search(message):
    surname = message.text
    bot.send_message(message.from_user.id, pro.Do_Commands('5', surname))

def Load(message):
    mes = message.text
    pro.Do_Commands('6', mes)

def Save(message):
    mes = message.text
    pro.Do_Commands('7', mes)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global textStr
    if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
        pro.Do_Commands('1', textStr) #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        textStr = ''
        bot.send_message(call.message.chat.id, 'Отмена')

bot.infinity_polling()