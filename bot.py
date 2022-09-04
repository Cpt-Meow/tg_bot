from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


proxy = {'proxy_url': settings.proxy_url,
         'urllib3_proxy_kwargs': {
             'username': settings.username,
             'password': settings.password
         }}


logging.basicConfig(filename='bot.log', format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def greet_user(update, context):
    print('Trigger /start')
    update.message.reply_text('Hello, user!')
    print(update)


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    mybot = Updater(settings.KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('bot started')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
