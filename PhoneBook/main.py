
#from email import message
from distutils.cmd import Command
from email import message
from View import UserInterface
from Controller import Controller
import contact_book 

import telebot

class Program:
    _Book = contact_book.contact_book()
    _ConPrint = None
    _Control = None
    _bot = None

    def __init__(self, Bot):
        self._bot = Bot
        self._ConPrint = UserInterface(self._bot)
        self._Control = Controller(self._Book, self._ConPrint, self._bot)
        self._Book.import_contact_list(self._Control.StartLoad())

    def Run(self):
        print('\nStart\n')
        return self._ConPrint.Print_Menu()
        #self._Book.import_contact_list(self._Control.StartLoad())

        #self._bot = telebot.TeleBot("5228215323:AAEKbGo5nILd9gYYSIQTbd1EYQq441G7PO8", parse_mode=None)

        #elf._ConPrint = UserInterface(self._bot)
        #self._Control = Controller(self._Book, self._ConPrint, self._bot)

        #self._bot.infinity_polling()

        print('Finish')

    def Do_Commands(self, message, id_command):
        #print(id_command)
        #self._ConPrint.Print_Menu()

        if id_command == '0':
            return False
        elif id_command == '1':
            self._Control.Add_User(message)
        elif id_command == '2':
            self._Control.Print_Book()
        elif id_command == '3':
            self._Control.Delite()
        elif id_command == '4':
            self._Control.Search(1)
        elif id_command == '5':
            self._Control.Search(2)
        elif id_command == '6':
            self._Book.import_contact_list(self._Control.Load_Data())
        elif id_command == '7':
            self._Control.Save_Data(self._Book.get_sorted())
            
        return 'message.text' + id_command    

    def Send_Mesage(self):
        self._bot.send_message('Send_Mesage')


bot = telebot.TeleBot("5228215323:AAEKbGo5nILd9gYYSIQTbd1EYQq441G7PO8", parse_mode=None)


pro =  Program(bot)
pro.Run()

me = bot.get_me()

@bot.message_handler(commands = 'menu')
def send_welcome(message):
    bot.reply_to(message, pro.Run())
    #pro.Do_Commands('1')
	#bot.reply_to(message, "Телефонная книга:\nHi")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    #print(message)
	bot.send_message(chat_id = message.chat.id , text = pro.Do_Commands(message, message.text))


bot.infinity_polling()

#pro =  Program()
#pro.Run()