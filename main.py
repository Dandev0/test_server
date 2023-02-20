import time
import requests


def send_log_tg(args):
    i = 0
    while True:
        i += 1
        url = f'https://api.telegram.org/bot5949160126:AAFQsXbwIRNLZgqOTqHnt_MiBAjiV-HT6cQ/sendMessage?chat_id=-799241823&text={args}&parse_mode=HTML'
        requests.get(url)
        time.sleep(5)
        if i == 10:
            break


if __name__ == '__main__':
    send_log_tg('Тестовое сообщение!')