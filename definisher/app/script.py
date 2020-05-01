import json, requests, urllib3
from bs4 import BeautifulSoup

def getContent(title):
    JSONData =  requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles="+title+"&exintro=1&explaintext=1")
    #takes title and gets intro of article
    JSONData = json.loads(JSONData.text)
    JSONData =  list(JSONData["query"]["pages"].values())[0]
    clearData = JSONData["extract"]
    return clearData
    #returns intro's text


def do(category=None):
    #if category's given, then it search random in category, else - just search random article
    if category:
        rand = requests.get("https://en.wikipedia.org/wiki/Special:RandomInCategory/" + str(category))
        rand.url = rand.url.replace("Category:", '')
        rand.url = rand.url.replace("Talk:", '')
        rand = requests.get(rand.url)

    else:
        rand = requests.get("https://en.wikipedia.org/wiki/Special:Random")

    soup = BeautifulSoup(rand.text, "html.parser")
    title = soup.h1.text

    #try to get content and if title has spaces, it changes 'em to "_" because of url needs
    try:
        content = getContent(title.replace(" ", "_"))
        print("done")

    #yeaah sometimes there is a keyError, idk why tho, so if this happends - recursion :)
    except KeyError:
        print(category)
        print("keyError")
        return do(category)

    #same as above - recursion
    if title==content or content==0:
        print(title)
        return do(category)

    else:
        print("fine")
        return title, content, rand.url
        #it returns following things which are needed
