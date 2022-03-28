import schedule
import time
import requests
from message.send_ml_init import send


def job():
    # event start crawler
    #r1 = requests.post('http://mercury-crawler-service:8888/crawler/ALL')
    #print(r1.status_code)
    #print(r1.headers['content-type'])
    #print(r1.encoding)
    #print(r1.text)
    # event end crawler

    # event start tech analysis
    #r2 = requests.post('http://mercury-data-analysis-service:5000/tech/analysis/ALL')
    #print(r2.status_code)
    #print(r2.headers['content-type'])
    #print(r2.encoding)
    #print(r2.text)
    # event end crawler

    send()


schedule.every(15).minutes.do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)


