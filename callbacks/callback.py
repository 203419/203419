# CALLBACKS 

import requests
import threading

def get_services1(response_json_data):
    name = response_json_data.get('results')[0].get('name').get('first')
    print(name)


def get_error1():
    print('Error')


def get_services2(response_json_data):
    name = response_json_data.get('results')[0].get('name').get('first')
    print(name)


def get_error2():
    print('Error')


def request_data(url, success_callback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()


class Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        h1 = threading.Thread(target=request_data, kwargs={'url':'https://randomuser.me/api/',
                                                    'success_callback': get_services1, 
                                                    'error_callback': get_error1})
        h1.start()

        h2 = threading.Thread(target=request_data, kwargs={'url':'https://randomuser.me/api/',
                                                    'success_callback': get_services2, 
                                                    'error_callback': get_error2})
        h2.start()

t = Thread()
t.start()