import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title="Please Drink Water",
            message="Drinking water is good for health.",
            app_icon="E:\YouTube\icon.ico",
            timeout=5
        )
        time.sleep(60*60)


        #it repeats after 60min (1hr).
