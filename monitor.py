import requests

URL = "https://schedule.cf-grcon-isl-pakistan.com/schedule/grcon-isl-pakistan/WORK_National_VISA"

def main():
    r = requests.get(URL, timeout=20)
    text = r.text.lower()

    # apni website ke exact words ke mutabiq yeh change ho sakta hai
    if "no appointments available" in text or "no appointment available" in text:
        print("NO_SLOTS")
    else:
        print("POSSIBLE_SLOT_OPEN (check manually)")

if _name_ == "_main_":
    main()
