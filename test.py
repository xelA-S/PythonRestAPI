import requests

BASE = "http://127.0.0.1:5000/"

data=[{"likes":300,"name":"my first video","views":500},
{"likes":600,"name":"my second video","views":900},
{"likes":900,"name":"my third video","views":1400}]


response = requests.put(BASE + "video/1", data[1])
print(response.json())
input()
response = requests.get(BASE + "video/1")
print(response.json())
input()
response = requests.patch(BASE + "video/1",{"likes":40})
print(response.json())
input()
response= requests.delete(BASE + "video/1")
print(response)
input()
response = requests.get(BASE + "video/1")
print(response.json())

