import os
import logging
from notion.client import NotionClient
from telegram.ext import CommandHandler
from telegram.ext import Updater

from service import ServiceManager
from step import StepManager
from decorators import Telegram
from tools import TaskUtil

def main():
    global serviceManager

    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s [%(levelname)s] - %(name)s: %(message)s')

    token = {"telegramToken" : "826053335:AAHfsHmALQfAd9JOrfJZzyJFwoVbYZcCMkY"}

    serviceManager = ServiceManager.Manager.init(token)
    stepManager = StepManager.Manager(serviceManager)
    TaskUtil.hi()
    serviceManager.start()


if __name__ == '__main__':
    main()