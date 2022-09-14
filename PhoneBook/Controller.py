from View import UserInterface
import contact_book
from text_logger import text_logger

from Handler import JsonHandler, XMLHandler

import telebot

class Controller:

    _Book = None
    _Con_Print = None
    _Logger = text_logger()
    _JsonLogg = JsonHandler()
    _XMLLogg = XMLHandler()
    _Bot = None

    def __init__(self, book, conPrint, Bot):
        self._Book = book
        self._Con_Print = conPrint    
        self._Bot = Bot

    def Load_Data(self):
        self._Con_Print.Print_Menu_Load_Save(1)
        res = self._Con_Print.Read_Line()

        self.Do_Logger(1, f'Загружено через {res} - способ')

        if res == '1': 
            data = self._JsonLogg.importin()
            return data
        if res == '2':
            data = self._XMLLogg.importin()
            print(data)
            return data

    def Save_Data(self, Booklist):
        self._Con_Print.Print_Menu_Load_Save(2)
        res = self._Con_Print.Read_Line()

        if res == '1': 
            self._JsonLogg.export(Booklist)
        if res == '2':
           self._XMLLogg.export(Booklist)

        self.Do_Logger(1, f'Сохранено через {res} - способ')

    def StartLoad(self):
        self.Do_Logger(1, 'Файл загружен при запуске приложения')
        return self._XMLLogg.importin()

    def Search(self, id_Command):
        result = None
        try:
            if id_Command == 1:
                id = int(self._Con_Print.Read_Line('Введите id: '))
                result = self._Book.get_by_id(id)
                
                self.Search_correctly(result)

                self._Con_Print.Print_List_Book(result)
            else:
                surname = self._Con_Print.Read_Line('Введите фамилию: ')
                result = self._Book.get_by_surname(surname)

                self.Search_correctly(result)

                self._Con_Print.Print_List_Book(result)        
        except:
            self._Con_Print.Print_In_Display('error')
            self.Do_Logger(3, "Ошибка поиска! Тип поиска: {}".format(id_Command))
            return
            

    def Search_correctly(self, result):
        if result == [] or result == None:
            self._Con_Print.Print_In_Display('Не найден контакт!')
            self.Do_Logger(1, 'Не найден контакт')

    def Add_User(self, message):
        name = self._Con_Print.WriteLine(message, 'Введите имя: ')
        patronymic = self._Con_Print.WriteLine('Введите отчество: ')
        surname = self._Con_Print.WriteLine('Введите фамилию: ')
        number = self._Con_Print.WriteLine('Введите номер: ')

        self._Book.add_contact(name, patronymic, surname, number)

        contact = '{} - {} - {} - {}'.format(name, patronymic, surname, number)
        self.Do_Logger(1, 'Добавлен контакт: {}'.format(contact))

    def Print_Book(self):
        res = self._Book.get_sorted()
        #res = self._Book.get_unsorted()
        self._Con_Print.Print_List_Book(res)

    def Delite(self):
        id = self._Con_Print.Read_Line('Введите id для удоления: ')

        result = self._Book.delete_contact(int(id))

        if result:
            self.Do_Logger(1, 'Удален контакт id: {}'.format(id))
        else:
            self._Con_Print.Print_In_Display('error')
            self.Do_Logger(3, 'Ошибка при удалении контакта по id: {}'.format(id))

    def Do_Logger(self, index, message):
        if index == 1:
            self._Logger.INFO(message)
        elif index == 2:
            self._Logger.WARNING(message)
        else:
            self._Logger.ERROR(message)
