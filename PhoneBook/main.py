
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

        #self._Book.import_contact_list(self._Control.StartLoad())

    def Run(self):
        print('\nStart bot\n')
        return self._ConPrint.Print_Menu()

        print('Finish')

    def Do_Commands(self, id_command, text):

        if id_command == '0':
            return False
        elif id_command == '1':
            self._Control.Add_User(text)
        elif id_command == '2':
            return self._Control.Print_Book()
        elif id_command == '3':
            return self._Control.Delite(text)
        elif id_command == '4':
            return self._Control.Search(1, text)
        elif id_command == '5':
            return self._Control.Search(2, text)
        elif id_command == '6':
            return self._Book.import_contact_list(self._Control.Load_Data(text))
        elif id_command == '7':
            return self._Control.Save_Data(self._Book.get_sorted(), text)
            
        return 'message.text' + id_command    

    def Send_Mesage(self):
        self._bot.send_message('Send_Mesage')


#pro =  Program()
#pro.Run()