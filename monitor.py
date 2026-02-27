import requests
import os

URL = "https://schedule.cf-grcon-is1-pakistan.com/schedule/grcon-is1-pakistan/WORK_National_VISA"

TOKEN = os.environ["TG_BOT_TOKEN"]
CHAT_ID = os.environ["TG_CHAT_ID"]

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)

def check():
    r = requests.get(URL)
    text = r.text.lower()

    if "available" in text or "slot" in text:
        send("🚨 Greece appointment slot may be open! Check now:\n" + URL)
    else:
        print("No slot yet")

if __name__ == "__main__":
    check()
