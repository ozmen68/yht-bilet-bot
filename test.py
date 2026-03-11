import requests

TOKEN = "8334170823:AAEV3aTrgoJHSjsNq5qybt7sszdKiLrhxg0"
CHAT_ID = "-1003736768920"

url = f"https://api.telegram.org/bot8334170823:AAEV3aTrgoJHSjsNq5qybt7sszdKiLrhxg0/sendMessage?chat_id=-1003736768920&text=Test%20mesaji"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": "Kanal testi 🚄"
})
