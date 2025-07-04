import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Вітаю! Я бот TotemGpt.")

@bot.message_handler(commands=['signal'])
def send_signal(message):
    bot.reply_to(message, "🔔 Торговий сигнал: LONG ARBUSDT\nВхід: 0.3393\nTP: 0.3730\nSL: 0.3270")

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '', 200

@app.route('/')
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=os.getenv("WEBHOOK_URL") + "/" + TOKEN)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))