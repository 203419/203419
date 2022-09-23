
from threading import Thread
from threading import Lock
import pytube

mutex = Lock()

def get_video(url):
    video = pytube.YouTube(url)
    video.streams.first().download('./videos')

class Hilo(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        mutex.acquire()
        get_video(self.url)
        mutex.release()

urls = ["https://www.youtube.com/watch?v=bLvwe67mD1A","https://www.youtube.com/watch?v=wuz8EOsE-28","https://www.youtube.com/watch?v=DchINZTuVWQ","https://www.youtube.com/watch?v=MhOnMTGeWTc", "https://www.youtube.com/watch?v=5gFfVFKyUME"]

for i in urls:
    t = Hilo(i)
    t.start()