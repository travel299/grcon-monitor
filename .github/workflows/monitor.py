import requests
import time

URL = "https://schedule.cf-grcon-isl-pakistan.com/schedule/grcon-isl-pakistan/WORK_National_VISA"

def check_slots():
    try:
        response = requests.get(URL, timeout=10)
        if "No appointments available" in response.text:
            print("❌ No slots available")
        else:
            print("✅ Slot may be available! Check website")
    except Exception as e:
        print(f"Error checking the site: {e}")

if _name_ == "_main_":
    while True:
        check_slots()
        time.sleep(15)
