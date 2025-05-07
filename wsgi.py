from flask import Flask, request
from telegram import Update
from bot import app as telegram_app

flask_app = Flask(__name__)

@flask_app.route('/webhook', methods=['POST'])
def telegram_webhook():
    try:
        update = Update.de_json(request.get_json(), telegram_app.bot)
        telegram_app.process_update(update)
        return 'OK'
    except Exception as e:
        print(f"❌ Webhook Error: {str(e)}")
        return str(e), 500

@flask_app.route('/')
def home():
    return "BRACU Resource Bot is running! Use /start in Telegram."
