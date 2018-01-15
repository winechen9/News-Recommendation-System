import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
from cloudAMQP_client import CloudAMQPClient

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://cqvewdqp:Q8e7yxcQ0U--2FoHwGWF5BHiZ4l1HUFn@termite.rmq.cloudamqp.com/cqvewdqp"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"

def clearQueue(queue_url, queue_name):
    queue_client = CloudAMQPClient(queue_url, queue_name)

    num_of_messages = 0

    while True:
        if queue_client is not None:
            msg = queue_client.getMessage()
            if msg is None:
                print("Cleared %d messages" % num_of_messages)
                return
            num_of_messages += 1
    
if __name__ == '__main__':
    clearQueue(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)