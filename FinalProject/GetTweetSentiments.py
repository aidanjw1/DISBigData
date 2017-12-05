from IBManalysis import toneAnalyzer
import os
import json

tweet_data = []

def getSentiment():
    count = 0
    #for name in os.listdir('./Tweets/'):
    with open('./Tweets/@cavs.txt', 'r') as f:
        content = f.readlines();
        for line in content:
            print(line)
            try:
                tweet_info = toneAnalyzer(line, "@cavs")
            except:
                pass

            if (tweet_info['Sentiment']):
                count += 1
                #print tweet_info
                tweet_data.append(tweet_info)
    print(count)
    appendJSON(tweet_data)


def readJSON(team, sentiment):
    with open('./sentiment_data/tweet_data.json', 'r') as f:
        data = json.load(f)

    totalJoy = 0
    numJoy = 0
    numTeamTweets = 0
    for tweet in data:
        if (tweet['Team'] == team):
            numTeamTweets += 1
            if (tweet['Sentiment'].has_key(sentiment)):
                totalJoy += tweet['Sentiment'][sentiment]
                numJoy += 1

    print(1.0 * numJoy / numTeamTweets)


def writeJSON(tweet_data):
    with open('./sentiment_data/tweet_data.json', 'w') as f:
        json.dump(tweet_data, f)


def appendJSON(tweet_data):
    with open('./sentiment_data/tweet_data.json', 'r') as f:
        data = json.load(f)

    for tweet in tweet_data:
        data.append(tweet)

    writeJSON(data)

getSentiment()
#readJSON()
