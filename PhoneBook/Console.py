
import telebot

class Console:
    _Bot = None
    
    def __init__(self, Bot):
        self._Bot = Bot

    def WriteLine(self, message, line:str):
        telebot.TeleBot.send_message(chat_id = message.chat.id, text = line)
        return 'test'
        #_Bot.send_message(line)

    def ReadLine(self, line:str):
        return input(line)

    def Clear(self):
        print()