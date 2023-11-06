import httpx

bot_token = 'TG_BOT_TOKEN'
user_chat_id = 'USER_CHAT_ID'
message = 'HELLO'

def send_message():
    with httpx.Client() as client:
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        params = {'chat_id': user_chat_id, 'text': message}
        response = client.post(url, params=params)

send_message()
