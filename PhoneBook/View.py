
from email import message
from os import lseek
from Console import Console

import telebot

class UserInterface:
    con = Console()

    def __init__(self, Bot):
        self.con = Console()

    def Print_Menu(self):

        line = 'Телефонная книга:\nКоманды:\nadd - Добавить\nprint - Вывести на экран список\
        \ndelete - Удалить\nserid - Поиск по id\nser - Поиск по фамилии\nload - Загрузить\nsave - Сохранить\nexit - Выход'

        self.con.WriteLine(line)
        return line
    
    def Print_Menu_Load_Save(self, index):
        massage = ''
        if index == 1:
            message = 'Загрузить'
        else:
            message = 'Сохранить'
        
        line = '\nТелефонная книга\n 1 - {} с помощью json\n2 - {} с помощью html'.format(message, message)
        #return line
        self.con.WriteLine(line)

    def Read_Line(self, line = '\n\tВведите номер команды: '):
        return self.con.ReadLine(line)
    
    def Print_List_Book(self, lisrUsers):
        line = '\n Список контактов:'
        
        for User in lisrUsers:
            line += '\nid: {} name: {} patronymic: {} surname: {} number: {}'.format(
                User.id, User.name, User.patronymic, User.surname, User.number)
        
        self.con.WriteLine(line)
        return line
        
    def Print_In_Display(self, line:str):
        self.con.WriteLine(line)

    def WriteLine(self, line:str):
        #telebot.TeleBot.send_message(chat_id = message.chat.id, text = line)
        self.con.WriteLine(line)
        return 'test'
