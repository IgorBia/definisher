import requests
from bs4 import BeautifulSoup

def do(category):
    while True:
        if category:
            r = requests.get("https://en.wikipedia.org/wiki/Special:RandomInCategory/" + str(category))
            rightUrl = r.url.replace("Category:", '')
            rightUrl = rightUrl.replace("Talk:", '')
            if r.url!=rightUrl:
                r = requests.get(rightUrl)

        else:
            r = requests.get("https://en.wikipedia.org/wiki/Special:Random")

        soup = BeautifulSoup(r.text, "html.parser")
        print(soup.p.text)

        if soup.p.text.strip() and soup.p.text.strip()!="Other reasons this message may be displayed:":
            content = soup.h1.text + "SplittingSentense" + soup.p.text

            for x in list(range(0,20)):
                check = '[{0}]'.format(str(x))
                content = content.replace(check, "")

            return str(content).encode(), r.url
