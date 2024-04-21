import requests
from datetime import datetime, timezone

def check_service(url):
    try:
        response = requests.get(url + "/now")
        if response.status_code == 200:
            current_time_str = response.text.strip()
            current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            now = datetime.now(timezone.utc)
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