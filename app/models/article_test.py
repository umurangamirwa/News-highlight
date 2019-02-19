import unittest
from models import news
News = news.news

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Python Must Be Crazy','A thrilling new Python Series','https://icdn.turkiyegazetesi.com.tr/images/haberler/2019_02/buyuk/bitcoin-3-921-dolarda-1550561497.jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()


