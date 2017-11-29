import requests as rq
import sys
import string

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
            cleanedText.append(word)
    text = " ".join(cleanedText)
    return text

if __name__ == "__main__":
    try:
        team = sys.argv[1]
    except:
        team = "Minnesota_Timberwolves"
    print team
    get_cleaned_text(team)
    #print get_wiki(team)
