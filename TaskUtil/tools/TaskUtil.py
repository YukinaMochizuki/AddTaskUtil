from decorators import Telegram

@Telegram.addCommandHandler()
def hi():
    def addCommand(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    return addCommand