import os
import logging
from notion.client import NotionClient
from telegram.ext import CommandHandler
from telegram.ext import Updater

from decorators import Telegram
from tools import TaskUtil

class Manager(object):
    
    def __init__(self):
        pass

    def start(self):
        self._teleUpdater.start_polling()

    @classmethod
    def init(cls, token):
        serviceManager = Manager()

        serviceManager._token = token
        serviceManager.initTelegram()
        # initNotion()
        # serviceManager.start()
        return serviceManager

    def initTelegram(self):
        self._teleUpdater = Updater(token=self._token["telegramToken"], use_context=True)
        self._teleDispatcher = self._teleUpdater.dispatcher

    def initNotion(self):
        self._notionClient = NotionClient(token_v2="<token_v2>")

    @property
    def teleUpdater(self):
        return self._teleUpdater

    @property
    def teleDispatcher(self):
        return self._teleDispatcher

    @property
    def notionClient(self):
        return self._notionClient

    @teleUpdater.setter
    def teleUpdater(self, teleUpdater):
        self._teleUpdater = teleUpdater
    
    @teleDispatcher.setter
    def teleDispatcher(self, teleDispatcher):
        self._teleDispatcher = teleDispatcher

    @notionClient.setter
    def notionClient(self, notionClient):
        self._notionClient = notionClient