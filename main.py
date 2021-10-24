from bot.tgbot import tgbot

import telebot

def main():

    try:
        tgbot.infinity_polling()
    except Exception as e:
        raise Exception(e)
    
if __name__ == "__main__":
    main()