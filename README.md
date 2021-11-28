# Telegram bot for wildberries



supports commands:

1. `/get_brand 'article'` – the argument indicates the article, the bot sends a message with the product with the brand name, according to the specified article.

2. `/get_title 'article'` – the argument also indicates the article of the goods, the bot sends a message with the name of the goods, according to the specified article.



**How to run**
1. Create your bot. [How?](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
2. Clone repo `git clone https://github.com/cornhubius/TelegrammBotWildberries`
3. Create venv `pythom -m venv env`
4. install requirements `pip install -r requirements.txt`
5. create `.env` file with `TOKEN="YourToken"` or change: `updater = Updater("YourToken", use_context=True)` in `wildberriesBot.py`
6. `python wildberriesBot.py `
7. Done. Now you can send article

