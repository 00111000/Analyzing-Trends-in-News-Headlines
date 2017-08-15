
import requests
import schedule
import datetime
import time
import json
from bs4 import BeautifulSoup
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features


# >>> soup.find('title')
# 'Page title'
# >>> soup.find_all('title')
# ['Page title']

NLU = NaturalLanguageUnderstandingV1(version='',
                                     username='',
                                     password='')

FILE_COUNTER = 4

def RT():
    """
    Scrapes the website of Russia Today news network.
    :return: null
    """
    global FILE_COUNTER

    URL = 'http://www.rt.com/'

    try:

        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        filename = str(FILE_COUNTER) + '.txt'
        mode = 'a+'

        # Open a file for appending
        with open(filename, mode) as fp:

            # Write the date and time to file
            fp.write(datetime.datetime.today().strftime('%Y-%m-%d'))
            fp.write(', ')
            fp.write(time.strftime("%H:%M:%S"))
            fp.write('\n')

            # Start of Russia Today news
            fp.write('N RT\n')

            # Scrapes the website of Russia Today news network and writes news headlines to a file
            for ul_tag in soup.find_all('ul', {'class': 'main-promobox__list'}):
                for li_tag in ul_tag.find_all('li', {'class': 'main-promobox__item'}):
                    for headline in li_tag.find_all('a', {'class': 'main-promobox__link'}):

                        news_headline = headline.text.lstrip().replace('\n', '')

                        fp.write('H ')
                        fp.write(news_headline)
                        fp.write('\n')
                        fp.write('J ')
                        json.dump(NLU.analyze(text=news_headline, features=[features.Sentiment(), features.Emotion(), features.Entities()]), fp)
                        fp.write('\n')

        fp.close()

    except:
        print('Error opening the URL')

    return

def WT():
    """
    Scrapes the website of The Washington Times news network.
    :return: null
    """
    global FILE_COUNTER

    URL = 'http://www.washingtontimes.com/news/politics/'

    try:

        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        filename = str(FILE_COUNTER) + '.txt'
        mode = 'a+'

        # Open a file for appending
        with open(filename, mode) as fp:

            # Start of The Washington Times news
            fp.write('N WT\n')

            # Scrapes the website of The Washington Times news network and writes news headlines to a file
            for article_tag in soup.find_all('section', {'class': 'featured-articles'}):
                for headline in article_tag.find_all('h2', {'class': 'article-headline'}):
                    for title in headline.find_all('a'):

                        news_headline = title['title']

                        fp.write('H ')
                        fp.write(news_headline)
                        fp.write('\n')
                        fp.write('J ')
                        json.dump(NLU.analyze(text=news_headline, features=[features.Sentiment(), features.Emotion(), features.Entities()]), fp)
                        fp.write('\n')

        fp.close()

    except:
        print('Error opening the URL')

    return None

def CBC():
    """
    Scrapes the website of CBC news network.
    :return: null
    """
    global FILE_COUNTER

    URL = 'http://www.cbc.ca/news/politics'

    try:

        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        filename = str(FILE_COUNTER) + '.txt'
        mode = 'a+'

        # Open a file for appending
        with open(filename, mode) as fp:

            # Start of CBC news
            fp.write('N CBC\n')

            # Scrapes the website of CBC news network and writes news headlines to a file
            for ul_tag in soup.find_all('ul', {'class': 'moreheadlines-list'}):
                for li_tag in ul_tag.find_all('li'):
                    for headline in li_tag.find_all('a', {'class': 'pinnableHref pinnableHeadline'}):

                        news_headline = headline.text

                        fp.write('H ')
                        fp.write(news_headline)
                        fp.write('\n')
                        fp.write('J ')
                        json.dump(NLU.analyze(text=news_headline, features=[features.Sentiment(), features.Emotion(), features.Entities()]), fp)
                        fp.write('\n')

        fp.close()

    except:
        print('Error opening the URL')

    return None


def main():
    global FILE_COUNTER

    RT() # 5 news
    WT() # 15 news
    CBC() # 16 news

    FILE_COUNTER += 1

    return None


if __name__ == '__main__':
    schedule.every().day.at("11:00").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
