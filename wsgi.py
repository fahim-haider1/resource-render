from flask import Flask, request
from bot import app  # Your existing PTB Application
import os

server = Flask(__name__)

@server.route('/webhook/' + os.environ['TOKEN'], methods=['POST'])
def telegram_webhook():
    update = Update.de_json(request.get_json(), app.bot)
    app.process_update(update)
    return 'OK'

@server.route('/')
def health_check():
    return "BRACU Resource Bot is running!"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))