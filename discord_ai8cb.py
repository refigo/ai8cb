def send_message_to_discord_webhook(message):
    import requests
    import os
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    print(response.status_code, response.text)
