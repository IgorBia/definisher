import json, requests
from bs4 import BeautifulSoup

def getContent(title):
    JSONData =  requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles="+title+"&exintro=1&explaintext=1")
    JSONData = json.loads(JSONData.text)
    JSONData =  list(JSONData["query"]["pages"].values())[0]
    clearData = JSONData["extract"]
    return clearData


def do(category=None):

    if category:
        rand = requests.get("https://en.wikipedia.org/wiki/Special:RandomInCategory/" + str(category))

    else:
        rand = requests.get("https://en.wikipedia.org/wiki/Special:Random")

    rightUrl = rand.url.replace("Category:", '')
    rightUrl = rightUrl.replace("Talk:", '')
    rand = requests.get(rightUrl)
    soup = BeautifulSoup(rand.text, "html.parser")
    title = soup.h1.text

    try:
        content = getContent(title.replace(" ", "_"))
        print("done")

    except KeyError:
        print(category)
        print("keyError")
        return do(category)

    if title==content or content==0:
        print(title)
        return do(category)

    else:
        print("fine")
        return title, content, rand.url
        
