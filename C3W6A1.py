import urllib.request , urllib.parse , urllib. error
import json
import ssl
import socket
#json file interact
#neha
ctx.check_hostname = False

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 0;
#This is a change by Jeevan Jyoti Sahoo
url = input('Enter URL')
data = urllib.request.urlopen(url).read().decode()

js = json.loads(data)
print(json.dumps(js,indent=4))

for item in js['comments']:
    count = count + item['count']
print(count)
a=5
b=6
print(a+b)*(a**b)

 
hostname = socket.gethostname() 
IPAddr = socket.gethostbyname(hostname) 
print("Your Computer Name is:" + hostname) 
print("Your Computer IP Address is:" + IPAddr) 


print("chnages by pravakar")
