from View import UserInterface
import contact_book
from text_logger import text_logger

class Controller:

    _Book = contact_book.contact_book()
    _Con_Print = UserInterface()
    _Logger = text_logger()

    def __init__(self, book, conPrint):
        self._Book = book
        self._Con_Print = conPrint    

    def Load_Data(self):
        self._Con_Print.Print_Menu_Load_Save(1)
        res = self._Con_Print.Read_Line()
        if res == '1': 
            return
        if res == '2':
            return
        #вместо return будет реализация  

    def Load_Save(self):
        self._Con_Print.Print_Menu_Load_Save(2)
        res = self._Con_Print.Read_Line()
        if res == '1': 
            return
        if res == '2':
            return
        #вместо return будет реализация  

    def StartLoad(self):
        self._Book._contacts = []
        self.Do_Logger(1, 'Файл загружен при запуске приложения')

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

                for user in result:
                    self._Con_Print.Print_List_Book(user)        
        except:
            self._Con_Print.Print_In_Display('error')
            self.Do_Logger(3, "Ошибка поиска! Тип поиска: {}".format(id_Command))
            return
            
        self._Con_Print.Read_Line('')

    def Search_correctly(self, result):
        if result == [] or result == None:
            self._Con_Print.Print_In_Display('Не найден контакт!')
            self.Do_Logger(1, 'Не найден контакт')

    def Add_User(self):
        name =   self._Con_Print.Read_Line('Введите имя: ')
        patronymic = self._Con_Print.Read_Line('Введите отчество: ')
        surname = self._Con_Print.Read_Line('Введите фамилию: ')
        number = self._Con_Print.Read_Line('Введите номер: ')

        self._Book.add_contact(name, patronymic, surname, number)

        contact = '{} - {} - {} - {}'.format(name, patronymic, surname, number)
        self.Do_Logger(1, 'Добавлен контакт: {}'.format(contact))

    def Print_Book(self):
        res = self._Book.get_unsorted()
        self._Con_Print.Print_List_Book(res)

    def Delite(self):
        id = self._Con_Print.Read_Line('Введите id для удоления: ')
        try:
            self._Book.delete_contact(int(id))
            self.Do_Logger(1, 'Удален контакт id: {}'.format(id))
        except:
            self._Con_Print.Print_In_Display('error')
            self.Do_Logger(3, 'Ошибка при удалении контакта по id: {}'.format(id))

    def Do_Logger(self, index, message):
        if index == 1:
            self._Logger.INFO(message)
        elif index == 2:
            self._Logger.WARNING(message)
        else:
            self._Logger.ERROR(message)
