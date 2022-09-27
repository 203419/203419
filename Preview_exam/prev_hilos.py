
import time
from threading import Thread, Lock
from weakref import finalize
import requests

mutex = Lock()

urls = ["https://www.seasjdlkewmoweo.com", "https://www.google.com", "https://www.facebook.com", "https://www.yahoo.com", 
        "https://www.iowphfuhawfpuia.com", "https://www.wikipedia.org", "https://www.reddit.com", "https://www.twitter.com", 
        "https://www.se31280hdho4ew4.com", "https://www.linkedin.com", "https://www.tumblr.com", "https://www.pinterest.com", 
        "https://www.845gjigjvsjokopijoi.com", "https://www.ebay.com", "https://www.microsoft.com", "https://www.imgur.com", 
        "https://www.craigslist.org", "https://www.bing.com", "https://www.stackoverflow.com", "https://www.apple.com", 
        "https://www.adobe.com", "https://www.office.com", "https://www.paypal.com", "https://www.chase.com", 
        "https://www.dropbox.com"]


def check_site(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            time.sleep(4)
            response = requests.head(url)
            if response.status_code == 200:
                print(f"El sitio {url} esta activo")
            else:
                print(f"El sitio {url} esta inactivo")
        else:
            print(f"El sitio {url} esta inactivo")
    except:
        print(f"El sitio {url} esta inactivo")      


class Hilo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        mutex.acquire()
        check_site(self.url)
        mutex.release()

t1 = [Hilo(urls[0]), Hilo(urls[1]), Hilo(urls[2]), Hilo(urls[3]), Hilo(urls[4]), Hilo(urls[5]), Hilo(urls[6]), Hilo(urls[7]), Hilo(urls[8]), 
        Hilo(urls[9]), Hilo(urls[10]), Hilo(urls[11]), Hilo(urls[12]), Hilo(urls[13]), Hilo(urls[14]), Hilo(urls[15]), Hilo(urls[16]), Hilo(urls[17]), 
        Hilo(urls[18]), Hilo(urls[19]), Hilo(urls[20]), Hilo(urls[21]), Hilo(urls[22]), Hilo(urls[23]), Hilo(urls[24])]

time_start = time.time()

for t in t1:
    t.start()

time_end = time.time()

print(f'El tiempo de ejecucion fue de {time_end - time_start } segundos')




        

    
