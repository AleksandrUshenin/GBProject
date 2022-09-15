
from email import message
import telebot

class Console:
    _Bot = None #telebot.TeleBot()
    
    def __init__(self, Bot):
        self._Bot = Bot

    def WriteLine(self, message, line:str):
        #telebot.TeleBot.send_message(chat_id = message.chat.id, text = line)
        return 'test'
        #_Bot.send_message(line)

    def ReadLine(self, message, line:str):
        #text = name = message.text
        return input(line)

    def Clear(self):
        print()