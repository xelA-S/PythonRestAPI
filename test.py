import requests

BASE = "http://127.0.0.1:5000/"

data=[{"likes":300,"name":"my first video","views":500},
{"likes":600,"name":"my second video","views":900},
{"likes":900,"name":"my third video","views":1400}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
    



response = requests.delete(BASE + "video/0")
print(response)