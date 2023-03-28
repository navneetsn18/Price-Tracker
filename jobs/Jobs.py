import schedule
import time

def job():
    # This method will check the current price and will compare the price
    return

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
