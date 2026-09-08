import requests
r=requests.get('http://google.co.kr')
print(r.text)