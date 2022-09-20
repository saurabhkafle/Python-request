import requests
from bs4 import BeautifulSoup


s = requests.session()
url = 'https://0a69009103955fa2c041ad65000a00ff.web-security-academy.net/login'
payload = {'csrf': 'az5SOwEcelcPvTgbIhamuuIuAUQ2CJ8e', 'username': 'pass', 'password': 'pass'}
cookies = {'session': 'A8WgZgigAkdYkBIVkjZbEwK5B8R2GEoS'}
r = s.post(url, data=payload, cookies=cookies)
print(r.text)

test = ["'","\"","`","1","2","3"]
xss = ['><h1>Test</h1>','\'><script>alert(1);</script>']
output = ['<h1>Test</h1>','<script>alert(1);</script>']
gg = 'https://0ab10029036e8bcec04f0b9100c8004d.web-security-academy.net/filter?category='
for i in test:
    url = gg+i
    print(url)
    req = requests.get(url)
    if "Internal Server Error" in req.text:
        print("Found SQLI based error")
        break
    else:
        print("No SQLI found")