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
    print(data[0])

    #print (data)



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







