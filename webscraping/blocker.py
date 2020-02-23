import time
from datetime import datetime as dt

Wsites = ["www.facebook.com","facebook.com","https://www.google.com","google.com","yahoo.com"]

host_path = r"/etc/hosts"
temp = r"hosts"
redirect = "127.0.0.1"

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours",dt.now())
        with open(host_path,'+r') as file:
            content = file.read()
            for website in Wsites:
                if website in content:
                    pass
                else:
                    file.write(redirect +" "+website+ "\n")
    else:
        with open(host_path,'+r') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in Wsites):
                    file.write(line)
            file.truncate()
        print(">>>>>>>HAVE FUNE>>>>>>>")
    time.sleep(1)