from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


# proxy = {'proxy_url': settings.proxy_url,
#          'urllib3_proxy_kwargs': {
#              'username': settings.username,
#              'password': settings.password
#          }}
#

logging.basicConfig(filename='bot.log',
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)


def greet_user(update, context):
    print('Trigger /start')
    update.message.reply_text('Hello, user!')
    print(update)


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def get_info_planets(update, context):
    now = datetime.datetime.now()
    dt_now = now.strftime('%d.%m.%Y %H:%M')
    planets = update.message.text.split()[1]
    planets_os = getattr(ephem, planets)
    update.message.reply_text(f'{planets} сегодня ({dt_now}) находится в созвездии {ephem.constellation(planets_os(dt_now))}')


def main():
    mybot = Updater(settings.KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_info_planets))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('bot started')
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
