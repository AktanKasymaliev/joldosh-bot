from bot.tgbot import tgbot

import logging, telebot

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

def main():

    try:
        tgbot.infinity_polling()
    except Exception as e:
        logger.error(e)
    
if __name__ == "__main__":
    main()