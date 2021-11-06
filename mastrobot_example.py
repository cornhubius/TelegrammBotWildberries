from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup
import os
import dotenv

dotenv.load_dotenv('.env')

def brand_name(article):
    url = f'https://www.wildberries.ru/catalog/{article}/detail.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('h1', class_="same-part-kt__header")
    quotes = [x.text for x in quotes]
    quotes = quotes[0].split('/')
    return quotes

 

def start(update, context):
    update.message.reply_text('/get_brand "article" | /get_title "article"')

def get_brand(update, context):
    res = brand_name(context.args[0])
    update.message.reply_text(res[0])

def get_title(update, context):
    res = brand_name(context.args[0])
    update.message.reply_text(res[1])

def error(update, context):
    update.message.reply_text('only 2 commands are temporarily supported: /get_brand "article" | /get_title "article"')

def main():
    TOKEN = os.environ.get('TOKEN')

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("get_brand", get_brand, pass_args=True))
    dispatcher.add_handler(CommandHandler("get_title", get_title, pass_args=True))
    dispatcher.add_error_handler(error)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()