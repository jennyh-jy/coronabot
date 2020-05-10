import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
CHAT_ID = os.environ.get('CHAT_ID', '')

if not TELEGRAM_TOKEN or not CHAT_ID:
    raise Exception('Check either TELEGRAM_TOKEN or CHAT_ID!')
