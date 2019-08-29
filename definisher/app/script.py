import requests
from bs4 import BeautifulSoup

def do():
    while True:
        r = requests.get('https://en.wikipedia.org/wiki/Special:Random')
        soup = BeautifulSoup(r.text, 'html.parser')
        p = soup.p
        soupP = BeautifulSoup(p.text, 'html.parser')
        if p.text.strip():
            content = soup.h1.text + "SplittingSentense" + soupP.text
            for x in list(range(0,20)):
                check = '[{0}]'.format(str(x))
                content = content.replace(check, '')
            return str(content).encode()
