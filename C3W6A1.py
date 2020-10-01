import urllib.request , urllib.parse , urllib. error
import json
import ssl

#json file interact
ctx.check_hostname = False

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 0;
url = input('Enter URL')
data = urllib.request.urlopen(url).read().decode()

js = json.loads(data)
print(json.dumps(js,indent=4))

for item in js['comments']:
    count = count + item['count']
print(count)



