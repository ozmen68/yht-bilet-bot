import requests

TOKEN = "8334170823:AAEV3aTrgoJHSjsNq5qybt7sszdKiLrhxg0"
CHAT_ID = "-1003736768920"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "Kanal testi 🚄"
})
