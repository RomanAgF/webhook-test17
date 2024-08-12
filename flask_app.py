from flask import Flask, request
import requests

app = Flask(__name__)

# Замените на ваш токен бота и ID чата
TELEGRAM_TOKEN = '7347761889:AAHgevNf0ec57pYLhrKB8JZ8yWOFRPllj24'
TELEGRAM_CHAT_ID = '613505553'

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=data)
    return response

@app.route('/webhook', methods=['POST'])
def webhook():
    # Получаем данные из вебхука
    data = request.form.to_dict()
    
    # Формируем сообщение
    event = data.get('event')
    fields = data.get('data[FIELDS][ID]')
    message = f'Event: {event}\nLead ID: {fields}'
    
    # Отправляем сообщение в Telegram
    send_telegram_message(message)
    
    return 'OK'

if __name__ == '__main__':
    app.run(port=5000)






