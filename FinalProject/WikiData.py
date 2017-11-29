import requests as rq
import sys

def get_wiki(team):
    url = "https://en.wikipedia.org/w/api.php?action=query&titles={0}&prop=revisions&rvprop=content&format=json".format(
        team)
    d = rq.get(url).text
    return d

if __name__ == "__main__":
    try:
        team = sys.argv[1]
    except:
        team = "Minnesota_Timberwolves"
    print team
    print get_wiki(team)
