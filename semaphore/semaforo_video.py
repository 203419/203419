
from threading import Semaphore, Thread
import pytube

semaforo = Semaphore(1)

def get_video(url):
    video = pytube.YouTube(url)
    video.streams.first().download('./videos')

class Hilo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        semaforo.acquire()
        get_video(self.url)
        semaforo.release()

urls = ["https://www.youtube.com/watch?v=bLvwe67mD1A","https://www.youtube.com/watch?v=wuz8EOsE-28","https://www.youtube.com/watch?v=DchINZTuVWQ","https://www.youtube.com/watch?v=MhOnMTGeWTc", "https://www.youtube.com/watch?v=5gFfVFKyUME"]

threads_semaphore = [Hilo(urls[0]), Hilo(urls[1]), Hilo(urls[2]), Hilo(urls[3]), Hilo(urls[4])]

for t in threads_semaphore:
    t.start()

