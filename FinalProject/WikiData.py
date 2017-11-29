import requests as rq
import sys
import string
from bs4 import BeautifulSoup
import re

badWords = list(string.punctuation)
numbers = ["0","1","2","3","4","5","6","7","8","9"]
badWords = badWords + numbers;
badWords.remove(".")
badWords.remove(",")
badWords.remove("?")
badWords.remove("!")

def get_wiki_markup(team):
    url = "https://en.wikipedia.org/w/api.php?action=query&titles={0}&prop=revisions&rvprop=content&format=json".format(
        team)
    d = rq.get(url).text
    return d

def get_cleaned_text(team):
    text = get_wiki_markup(team)
    words = text.split(" ")
    cleanedText = []
    for word in words:
        check = True
        for badWord in badWords:
            if badWord in word or word == "" or len(word) < 5:
                check = False
                break
        if (check == True):
            cleanedText.append(word, 'html.parser')
    text = " ".join(cleanedText)
    return text

def get_history_text(team):
    out = ''
    url = "https://en.wikipedia.org/wiki/{0}".format(team)
    html = rq.get(url).text
    soup = BeautifulSoup(html)
    history = soup.find_all('div', attrs={'id': 'mw-content-text'})
    p = history[0].find_all('p')
    for i in p:
        i = str(i)
        i = re.sub('<.*?>', '', i)
        out += ' ' + i
    return out




if __name__ == "__main__":
    try:
        team = sys.argv[1]
    except:
        team = "Minnesota_Timberwolves"
    print get_history_text(team)
