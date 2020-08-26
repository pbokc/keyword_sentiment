from textblob import TextBlob
import requests
from bs4 import BeautifulSoup


class Analysis:

    def __init__(self, term):
        self.term = term
        self.sentiment = 0
        self.subjectivity = 0

        self.url = 'http://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)

        print('URL----->', self.url)

    def run(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headline_results = soup.find_all('div', attrs={'class': 'ZINbbc'})

        blob = []
        titles = []

        for h in headline_results:
            try:
                blob = TextBlob(h.find('div', attrs={'class': 'BNeawe'}).get_text())
                if blob != '':
                    titles.append(blob)
            except:
                continue

            self.sentiment += blob.sentiment.polarity / len(headline_results)
            self.subjectivity += blob.sentiment.subjectivity / len(headline_results)

