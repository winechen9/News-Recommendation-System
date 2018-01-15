import os
import sys




sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))
import cnn_news_scraper
from cloudAMQP_client import CloudAMQPClient

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://fmzvgwat:VUzmxL2eF3c_QZ-4m9StmUCf8WALe8Z8@termite.rmq.cloudamqp.com/fmzvgwat"
DEDUPE_NEWS_TASK_QUEUE_NAME = "tap-news-dedupe-news-task-queue"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://cqvewdqp:Q8e7yxcQ0U--2FoHwGWF5BHiZ4l1HUFn@termite.rmq.cloudamqp.com/cqvewdqp"
SCRAPE_NEWS_TASK_QUEUE_NAME = "tap-news-scrape-news-task-queue"


SLEEP_TIME_IN_SECONDS = 5

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print('message is broken')
        return

    task = msg
    text = None

    if task['source'] == 'cnn':
        print('scraping CNN news')
        text = cnn_news_scraper.extractNews(task['url'])
    else:
        print('News source [%s] is not supported.' % task['source'])

    task['text'] = text
    dedupe_news_queue_client.sendMessage(task)


while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            # Parse and process the task
            try:
                handle_message(msg)
            except Exception as e:
                print(e)
                pass
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
