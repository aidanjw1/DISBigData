from IBManalysis import toneAnalyzer
import os
import json

tweet_data = []
#out = []

def getSentiment():
    #for name in os.listdir('./Tweets/'):
    with open('./Tweets/@ATLHawks.txt', 'r') as f:
        content = f.readlines();
        for line in content:
            tweet_info = toneAnalyzer(line, name[:-4])

            if (tweet_info['Sentiment']):
                print tweet_info
                tweet_data.append(tweet_info)
    print (tweet_data)


def readJSON():


def writeJSON():

'''for team in team_data.keys():
    team_tones = {}
    team_tones['team'] = team
    for tone in team_data[team]:
        team_tones[tone['tone_name']] = str(tone['score'])
    out.append(team_tones)
    print 'json added: ' + team'''

'''with open('./sentiment_data/history_sentiments.json', 'w') as f:
    json.dump(out, f)'''

getSentiment()