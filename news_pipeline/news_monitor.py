import hashlib
import redis
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import news_api_client

while True:
    news_list = news_api_client.getNewsFromSource(NEWS_SOURCES)

    number_of_news = 0

    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8')).hexdigest()

        if redis_client.get(news_digest) is None:
            number_of_news += 1
            