from flask import Flask, request
import requests

app = Flask(__name__)

# Замените на ваш токен бота и ID чата
TELEGRAM_TOKEN = '7201807860:AAFrdTVZaZfNNUWi70SV1mKibsItmveEItQ'
TELEGRAM_CHAT_ID = '352566109'

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
    message = f'Название события: {event}\ ID Сделки: {fields}'
    
    # Отправляем сообщение в Telegram
    send_telegram_message(message)
    
    return 'OK'

if __name__ == '__main__':
    app.run(port=5000)






