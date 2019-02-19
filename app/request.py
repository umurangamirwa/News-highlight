from app import app
import urllib.request,json
from .models import article, source

News = source.News
# Getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
            print(news_results)
    
    return news_results
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
       news_list: A list of dictionaries that contain news details

    Returns :
       news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('name')
        overview = news_item.get('description')
        # content = news_item.get('content')
        # publishedAt = news_item.get('publishedAt')
        news_object = News(id,title,overview)
        news_results.append(news_object)

    return news_results
def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/sources?api_Key={}&query={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            # search_news_articles = process_results(search_news_list)


    return search_news_articles


