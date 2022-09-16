from tkinter import E
from main import Program
import telebot

name = ''
patronymic = ''
surname = ''
number = ''

bot = telebot.TeleBot("5228215323:AAEKbGo5nILd9gYYSIQTbd1EYQq441G7PO8", parse_mode=None)

pro =  Program(bot)
pro.Run()

me = bot.get_me()

@bot.message_handler(commands = 'menu')
def send_welcome(message):
    bot.reply_to(message, pro.Run())
    #pro.Do_Commands('1')
	#bot.reply_to(message, "Телефонная книга:\nHi")

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
    number = message.text
    text = f'{name} {patronymic} {surname} {number}'
    bot.send_message(message.from_user.id, f'User = {text}')
    pro.Do_Commands('1', text)

def Delete(message):
    global id
    id = int(message.text)
    bot.send_message(message.from_user.id, pro.Do_Commands('3', ''))

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

bot.infinity_polling()