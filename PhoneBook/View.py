
from email import message
from os import lseek
from Console import Console

import telebot

class UserInterface:
    con = None

    def __init__(self, Bot):
        self.con = Console(Bot)

    def Print_Menu(self):

        line = 'Телефонная книга:\nКоманды:\n1 - Добавить\n2 - Вывести на экран список\
        \n3 - Удалить\n4 - Поиск по id\n5 - Поиск по фамилии\n6 - Загрузить\n7 - Сохранить\n0 - Выход'

        #self.con.WriteLine(line)
        return line
    
    def Print_Menu_Load_Save(self, index):
        massage = ''
        if index == 1:
            message = 'Загрузить'
        else:
            message = 'Сохранить'
        
        line = '\nТелефонная книга\n 1 - {} с помощью json\n2 - {} с помощью html'.format(message, message)
        self.con.WriteLine(line)

    def Read_Line(self, line = '\n\tВведите номер команды: '):
        return self.con.ReadLine(line)
    
    def Print_List_Book(self, lisrUsers):
        line = '\n Список контактов:'
        
        for User in lisrUsers:
            line += '\nid: {} name: {} patronymic: {} surname: {} number: {}'.format(
                User.id, User.name, User.patronymic, User.surname, User.number)

        self.con.WriteLine(line)
        
    def Print_In_Display(self, line:str):
        self.con.WriteLine(line)

    def WriteLine(message, line:str):
        telebot.TeleBot.send_message(chat_id = message.chat.id, text = line)
        return 'test'
