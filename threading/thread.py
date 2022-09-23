
import threading
import requests
import time
import psycopg2
import pytube

conexion = psycopg2.connect(user='postgres', password='sebasramirez11', host='localhost', port='5432', database='api')
urls = ["https://www.youtube.com/watch?v=bLvwe67mD1A","https://www.youtube.com/watch?v=wuz8EOsE-28","https://www.youtube.com/watch?v=DchINZTuVWQ","https://www.youtube.com/watch?v=MhOnMTGeWTc", "https://www.youtube.com/watch?v=5gFfVFKyUME"]

lock = threading.Lock()

def get_name():
    response = requests.get('https://randomuser.me/api/?results=2000')

    if response.status_code == 200:
        results = response.json().get('results')
        for name in results: 
            write_db(name['name']['first'])

def write_db(x):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO names(name) VALUES('"+x+"')")
    conexion.commit()  
    cursor.close() 

def get_video(url):
    for i in url:
        video = pytube.YouTube(i)
        video.streams.first().download('./videos')

def get_user():
    response = requests.get('https://randomuser.me/api/')

    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)


if __name__ == "__main__":
    start_time = time.time()

    thread1 = threading.Thread(target=get_name)
    thread2 = threading.Thread(target=get_video(urls))

    thread1.start()
    thread2.start()
    
    for i in range(50):
        thread3 = threading.Thread(target=get_user)
        thread3.start()
        thread3.join()

    end_time = time.time()
    print(end_time - start_time)
    

