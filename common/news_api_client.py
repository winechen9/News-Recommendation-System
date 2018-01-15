import requests

from json import loads


NEWS_API_ENDPOINT = "https://newsapi.org/v1/"
NEWS_API_KEY = '1d11df480f5a4545bfb2b6c157643fa4'


ARTICLES_API = 'articles'

CNN = 'cnn'
DEFAULT_SOURCES = [CNN]
SORT_BY_TOP = 'top'


def _buildUrl(endPoint=NEWS_API_ENDPOINT, apiName=ARTICLES_API):
    return endPoint + apiName



def getNewsFromSource(sources=DEFAULT_SOURCES, sortBy=SORT_BY_TOP):
    articles = []

    for source in sources:
        payload = {'apiKey': NEWS_API_KEY, 'source': source, 'sortBy': sortBy}

        response = requests.get(_buildUrl(), params = payload)
        # maybe exists many languages
        res_json = loads(response.content.decode('utf-8'))

        # Extract news from response
        if (res_json is not None and 
            res_json['status'] == 'ok' and
            res_json['source'] is not None):
            # populate news source in each sources
            for news in res_json['articles']:
                news['source'] = res_json['source']
            articles.extend(res_json['articles'])

        return articles

