
import time
import requests

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


time_start = time.time()

for url in urls:
    check_site(url)
    time_end = time.time()

print(f'El tiempo de ejecucion fue de {time_end - time_start} segundos')
