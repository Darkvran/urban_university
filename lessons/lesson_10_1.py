from threading import Thread
import requests

THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
res = []
def func(url):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)

first = Thread(target=func, args =(THE_URL,))
second = Thread(target=func, args=(THE_URL,))
third = Thread(target=func, args=(THE_URL,))

first.start()
second.start()
third.start()

first.join()
second.join()
third.join()

print(res)