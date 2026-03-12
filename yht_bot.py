import requests

TOKEN = "8334170823:AAEV3aTrgoJHSjsNq5qybt7sszdKiLrhxg0"
CHAT_ID = "-1003736768920"

origin = "Konya"
destination = "Ankara GAR"

date = "2026-03-13"

target_times = ["15:25", "17:35"]


def send_telegram(msg):

    url = f"https://api.telegram.org/bot8334170823:AAEV3aTrgoJHSjsNq5qybt7sszdKiLrhxg0/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })


def check_yht():

    url = "https://yht-proxy.menozmen68.workers.dev/"

    payload = {
        "nereden": origin,
        "nereye": destination,
        "tarih": date
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": "https://ebilet.tcddtasimacilik.gov.tr",
        "Referer": "https://ebilet.tcddtasimacilik.gov.tr/"
    }

    r = requests.post(url, json=payload, headers=headers)

    print(r.text)

    data = r.json()

    if "seferler" not in data:
        return

    for sefer in data["seferler"]:

        saat = sefer["binisSaat"]

        if saat not in target_times:
            continue

        bos = sefer.get("bosKoltuk", 0)

        if bos <= 0:
            continue

        msg = f"""
🚄 YHT BILET BULUNDU

{origin} → {destination}
Tarih: {date}

Saat: {saat}
Bos koltuk: {bos}

https://ebilet.tcddtasimacilik.gov.tr
"""

        send_telegram(msg)


check_yht()
