import requests
from datetime import datetime
import pytz

def check_service(url):
    try:
        response = requests.get(url + "/now")
        if response.status_code == 200:
            current_time = datetime.strptime(response.text, "%Y-%m-%d %H:%M:%S")
            current_time = pytz.utc.localize(current_time)
            current_time = current_time.astimezone(pytz.utc)
            now = datetime.now(pytz.utc)
            time_difference = abs(now - current_time).total_seconds()
            if time_difference <= 1:
                return True
    except Exception as e:
        print("Error:", e)
    return False

if __name__ == "__main__":
    service_url = "http://13.211.202.215"
    if check_service(service_url):
        print("Service is synchronized.")
    else:
        print("Service is desynchronized.")