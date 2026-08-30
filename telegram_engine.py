import requests

from telegram_config import BOT_TOKEN
from telegram_config import CHAT_ID


def send_signal(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(
        url,
        data=payload
    )

    print(response.text)