import requests

TOKEN = "8334170823:AAEV3aTrgoJHSjsNq5qybt7sszdKiLrhxg0"
CHAT_ID = "-1003736768920"

origin_id = 1082
destination_id = 1088

date = "2026-03-13"

target_times = ["15:25", "17:35"]

def send_telegram(msg):

    url = f"https://api.telegram.org/bot8334170823:AAEV3aTrgoJHSjsNq5qybt7sszdKiLrhxg0/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })
send_telegram("Bot calisiyor testi 🚄")

def check_yht():

    url = "https://api-yebsp.tcddtasimacilik.gov.tr/sefer/seferSorgula"

    payload = {
        "neredenId": origin_id,
        "nereyeId": destination_id,
        "tarih": date
    }

    r = requests.post(url, json=payload)

    data = r.json()

    if "seferler" not in data:
        return False

    for sefer in data["seferler"]:

        saat = sefer["binisTarihSaat"][11:16]

        if saat in target_times:

            bos = sefer["bosKoltuk"]

            if bos > 0:

                msg = f"""
🚄 YHT BILET BULUNDU

Konya → Ankara
Tarih: {date}

Saat: {saat}
Bos koltuk: {bos}

https://ebilet.tcddtasimacilik.gov.tr
"""

                send_telegram(msg)
                return True

    return False


check_yht()
