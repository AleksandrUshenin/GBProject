
class Console:
    _Bot = None #telebot.TeleBot()
    
    #def __init__(self, Bot):
    #    self._Bot = Bot

    def WriteLine(self, line:str):
        print(line)

    def ReadLine(self, message, line:str):
        #text = name = message.text
        return input(line)

    def Clear(self):
        print()