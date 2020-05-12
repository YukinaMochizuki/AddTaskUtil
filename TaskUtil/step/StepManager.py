from decorators import Telegram


class Manager(object):

    def __init__(self, serviceManager):
        self._serviceManager = serviceManager
        stepCancel()
    


@Telegram.addCommandHandler()
def stepCancel():
    def addCommand(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Step Canael and exit!")
    return addCommand
