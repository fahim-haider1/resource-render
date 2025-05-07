from flask import Flask, request
from telegram import Update
from bot import app as telegram_app  # Import with alias
import os

# Initialize Flask app
flask_app = Flask(__name__)

@flask_app.route('/webhook/' + os.environ['TOKEN'], methods=['POST'])
def telegram_webhook():
    update = Update.de_json(request.get_json(), telegram_app.bot)
    telegram_app.process_update(update)
    return 'OK'

@flask_app.route('/')
def health_check():
    return "BRACU Resource Bot is running!"

if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))