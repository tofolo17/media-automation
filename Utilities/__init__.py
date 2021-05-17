import requests
from bs4 import BeautifulSoup


def get_url_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.get_text().encode('ascii', 'ignore').decode('ascii')
