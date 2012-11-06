#使用urlopen.read()判断url状态并反馈 
- tags: python, urllib2

----
####Source Code
```python
#!/usr/bin/env python
import os
import time
import urllib2
import telnetlib
import socket

socket.setdefaulttimeout(10.0)

expectTime = 5 # seconds
host = "127.0.0.1"
port = "80"
tomcat = "/usr/local/tomcat/"

def restartlocaltomcat():
    os.system("mv /var/log/tomcat_gc.log /var/log/tomcat_gc.log.`date +%Y%m%d`")
    os.system('echo "[`date`] Tomcat now to shutdowning, please wait 10 seconds .." >> tomcatstatus.log')
    os.system(tomcat + "bin/shutdown.sh")
    os.system("kill -9 `ps -C java --no-header | awk '{print $1}'`")
    time.sleep(10)
    try:
        tel = telnetlib.Telnet(host, port)
        os.system('echo "[`date`] Shutdown tomcat failed, please shutdown by yourself .." >> tomcatstatus.log')
    except:
        os.system('echo "[`date`] Shutdown tomcat success .." >> tomcatstatus.log')
        os.system('echo "[`date`] Tomcat now to starting .." >> tomcatstatus.log')
        os.system(tomcat + "bin/startup.sh")
        time.sleep(60)
        try:
            telnet = telnetlib.Telnet(host, port)
            os.system('echo "[`date`] Startup tomcat success .." >> tomcatstatus.log')
        except:
            os.system('echo "[`date`] Startup tomcat failed .." >> tomcatstatus.log')

while(True):
    try:
        startTime = time.time()
        #urllib2.urlopen("http://192.168.10.50/index.html").read()
        urllib2.urlopen("http://192.168.10.50/search?q=&sort=0&pageSize=4&isQueryTerm=0&sourceId=item.index").read()
        endTime = time.time()
    except Exception, e:
        restartlocaltomcat()
        time.sleep(5*60)
        continue
    if (int(endTime - startTime) > expectTime):
        restartlocaltomcat()
    #else:
    #	os.system('echo "[`date`] Tomcat status OK" >> tomcatstatus.log')
    time.sleep(5*60)
```

####How to use
```bash
[root@vh1 ~]# nohup python checkUrlTomcat.py &
```

