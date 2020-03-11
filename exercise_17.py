import requests
from bs4 import BeautifulSoup


def request_article_titles(url):
    request = requests.get(url)
    request_html = request.text
    article_finder = BeautifulSoup(request_html)
    title = article_finder.find('span', 'articletitle')
    return title


def main():
    request_article_titles('https://www.nytimes.com/')


if __name__ == '__main__':
    main()
