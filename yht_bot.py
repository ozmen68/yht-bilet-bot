import requests
import json
import os

TOKEN = "8334170823:AAEV3aTrgoJHSjsNq5qybt7sszdKiLrhxg0"
CHAT_ID = "-1003736768920"

origin_id = 1082
destination_id = 1088

date = "2026-03-13"

target_times = ["15:25", "17:35"]

sent_file = "sent_seferler.json"


def send_telegram(msg):

    url = f"https://api.telegram.org/bot8334170823:AAEV3aTrgoJHSjsNq5qybt7sszdKiLrhxg0/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })


def load_sent():

    if os.path.exists(sent_file):
        with open(sent_file) as f:
            return json.load(f)

    return []


def save_sent(data):

    with open(sent_file, "w") as f:
        json.dump(data, f)


def check_yht():

    url = "https://api-yebsp.tcddtasimacilik.gov.tr/sefer/seferSorgula"

    payload = {
        "neredenId": origin_id,
        "nereyeId": destination_id,
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

    sent = load_sent()

    for sefer in data["seferler"]:

        saat = sefer["binisTarihSaat"][11:16]

        if saat not in target_times:
            continue

        bos = sefer.get("bosKoltuk", 0)

        engelli = sefer.get("kalanEngelliKoltuk", 0)

        if bos <= 0:
            continue

        if bos == engelli:
            continue

        key = f"{date}_{saat}"

        if key in sent:
            continue

        msg = f"""
🚄 YHT BILET BULUNDU

Konya → Ankara
Tarih: {date}

Saat: {saat}
Bos koltuk: {bos}

https://ebilet.tcddtasimacilik.gov.tr
"""

        send_telegram(msg)

        sent.append(key)

    save_sent(sent)


check_yht()
