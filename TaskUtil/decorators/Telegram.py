from telegram.ext import CommandHandler
from telegram.ext import Updater
import __main__

def addCommandHandler():
    def decorator(func):
        def warp():
            __main__.serviceManager.teleDispatcher.add_handler(CommandHandler(func.__name__, func()))
        return warp
    return decorator