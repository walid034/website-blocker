import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect = "127.0.0.1"
sites = ["www.facebook.com", "facebook.com", "youtube.com", "www.youtube.com", "fb.com", "www.fb.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 19) <= dt.now() <= dt(dt.now().year, dt.now().month, dt.now().day, 23):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in sites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in sites):
                    file.write(line)
            file.truncate()
        # print("Still, try to study")
    time.sleep(10)
