import requests
import string, time
url = "https://disk.yandex.ru/d/udJ2T7T2-gdQ9Q"
urlQ = "https://disk.yandex.ru/d/udJ2T7T2-gdQ9Q"

alphabet = "Z"

qwerty = False

for i in range(25, len(url)):
    for c in alphabet:
        url = url[:i] + c + url[i + 1:]
        response = requests.get(url)
        print(url, "QQQQ")
        #time.sleep(0.01)
        if response.status_code == 200:
            print(url, "success")
            qwerty = True
            break
    if qwerty:
        break
    url = urlQ
