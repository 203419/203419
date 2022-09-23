import time
import concurrent.futures
import threading
from pytube import YouTube

threading_local = threading.local()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(get_service, url)

def get_service(url):
    SAVE_PATH = "./"

    link= url

    try:
        yt = YouTube(link)
    except:
        print("Connection Error") 

    stream = yt.streams.get_by_itag(22)

    try:
        stream.download(SAVE_PATH)
    except:
        print("Error")
    print('Completado')


if __name__ =="__main__":
    init_time= time.time()
    thread1 = threading.Thread(target=service, args=("https://www.youtube.com/watch?v=bLvwe67mD1A"))
    thread1.start()
    thread1.join()
    thread2 = threading.Thread(target=service, args=("https://www.youtube.com/watch?v=nyXffW_RQI4"))
    thread2.start()
    thread2.join()
    thread3 = threading.Thread(target=service, args=("https://www.youtube.com/watch?v=wuz8EOsE-28"))
    thread3.start()
    thread3.join()
    thread4 = threading.Thread(target=service, args=("https://www.youtube.com/watch?v=DchINZTuVWQ"))
    thread4.start()
    thread4.join()
    thread5 = threading.Thread(target=service, args=("https://www.youtube.com/watch?v=MhOnMTGeWTc"))
    thread5.start()
    thread5.join()
    end_time=time.time() - init_time
    print(end_time)