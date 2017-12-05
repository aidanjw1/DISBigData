from IBManalysis import toneAnalyzer
import os
import json

tweet_data = []
#out = []

def getSentiment():
    #for name in os.listdir('./Tweets/'):
    with open('./Tweets/@Bucks.txt', 'r') as f:
        content = f.readlines();
        for line in content:
            tweet_info = toneAnalyzer(line, "@Bucks")

            if (tweet_info['Sentiment']):
                print tweet_info
                tweet_data.append(tweet_info)
    #print (tweet_data)
    #writeJSON(tweet_data)
    appendJSON(tweet_data)


def readJSON():
    with open('./sentiment_data/tweet_data.json', 'r') as f:
        data = json.load(f)

    #print (json.dumps(data, indent=4, sort_keys=True))
    totalJoy = 0
    numJoy = 0
    numTeamTweets = 0
    for tweet in data:
        if (tweet['Team'] == "@BrooklynNets"):
            numTeamTweets += 1
            if (tweet['Sentiment'].has_key('Joy')):
                totalJoy += tweet['Sentiment']['Joy']
                numJoy += 1

    print(1.0 * numJoy / numTeamTweets)
    #print (data)



def writeJSON(tweet_data):
    with open('./sentiment_data/tweet_data.json', 'w') as f:
        cleaned_data = json.dumps(tweet_data, indent=4, sort_keys=True)
        json.dump(cleaned_data, f)


def appendJSON(tweet_data):
    with open('./sentiment_data/tweet_data.json', 'r') as f:
        data = json.load(f) 

    for tweet in tweet_data:
        data.append(tweet)

    writeJSON(data)

#getSentiment()
readJSON()







