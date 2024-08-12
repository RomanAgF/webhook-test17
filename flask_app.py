import requests
from flask import Flask, request

app = Flask(__name__)

# Вставь сюда свой токен Telegram
TELEGRAM_BOT_TOKEN = '7347761889:AAHgevNf0ec57pYLhrKB8JZ8yWOFRPllj24'
TELEGRAM_CHAT_ID = '613505553'

def send_message_to_telegram(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': text}
    response = requests.post(url, data=data)
    return response

# Добавляем обработчик вебхука
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json  # Получаем данные из POST-запроса
        print(f"Received data: {data}")  # Логируем полученные данные

        if 'event' in data:
            event_type = data['event']
            if event_type == 'ONCRMLEADADD':
                lead_title = data['data']['FIELDS']['TITLE']
                message = f'Новый лид создан: {lead_title}'
                send_message_to_telegram(message)
            elif event_type == 'ONCRMPRODUCTADD':
                product_name = data['data']['FIELDS']['NAME']
                message = f'Новый товар создан: {product_name}'
                send_message_to_telegram(message)
            else:
                message = 'Неизвестное событие.'
                send_message_to_telegram(message)

        return 'OK', 200
    except Exception as e:
        print(f"Error: {e}")  # Логируем ошибки, если они есть
        return 'Error', 500

@app.route('/')
def index():
    
    return 'Webhook is active. Please send data to /webhook endpoint.', 200

if __name__ == '__main__':
    app.run()
