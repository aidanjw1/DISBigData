import tweepy
import json

def get_tweets():
    consumer_key = 'dv6NWGg4QT8rr979x81KLIsyI'
    consumer_secret = 'nRVr5D48SWJhl491PRjMVCxpCUpnUdMPpbgWsDr920Dm6111vc'
    access_token = '4855652441-2Ku9RhnqT24ZyjvtyiqrLWUVqbbjNZILhcynw9u'
    access_token_secret = 'br2CEMNroCFKYPK8mckafFqhAiRXg6TwW2EhmZZC0riYT'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    team_tweets = {'@Raptors':[], '@warriors':[], '@nuggets':[],
                   '@okcthunder':[], '@PelicansNBA':[], '@dallasmavs':[],
                   '@hornets':[], '@Lakers':[], '@nyknicks':[],
                   '@Timberwolves':[], '@LAClippers':[], '@OrlandoMagic':[],
                   '@Pacers':[], '@cavs':[], '@HoustonRockets':[],
                   '@BrooklynNets':[], '@Suns':[], '@spurs':[], '@utahjazz':[],
                   '@celtics':[], '@ATLHawks':[], '@DetroitPistons':[],
                   '@chicagobulls':[], '@sixers':[], '@Bucks':[],
                   '@WashWizards':[], '@MiamiHEAT':[], '@memgrizz':[],
                   '@trailblazers':[], '@SacramentoKings':[]}

    for team in team_tweets.keys():
        f = open('./Tweets/' + team + '.txt', 'a')

        for tweet in tweepy.Cursor(api.search, q=team, lang='en', count=100).items(300):
            if not tweet.text[:2] == 'RT':
                f.write(tweet.text.encode('utf-8') + '\n')

        f.close()

def sentiment_ranks():
    teams = {'@Raptors':{}, '@warriors':{}, '@nuggets':{}, '@okcthunder':{},
             '@PelicansNBA':{}, '@dallasmavs':{}, '@hornets':{}, '@Lakers':{},
             '@nyknicks':{}, '@Timberwolves':{}, '@LaClippers':{},
             '@OrlandoMagic':{}, '@Pacers':{}, '@cavs':{}, '@HoustonRockets':{},
             '@BrooklynNets':{}, '@Suns':{}, '@spurs':{}, '@utahjazz':{},
             '@celtics':{}, '@ATLHawks':{}, '@DetroitPistons':{},
             '@chicagobulls':{}, '@sixers':{}, '@Bucks':{}, '@WashWizards':{},
             '@MiamiHEAT':{}, '@memgrizz':{}, '@trailblazers':{},
             '@SacramentoKings':{}}

    joy_dict = {}
    sadness_dict = {}
    anger_dict = {}

    # populate dicts with sentiment values
    for team in teams.keys():
        joy_dict[team] = average_sentiment(team, 'Joy')
        sadness_dict[team] = average_sentiment(team, 'Sadness')
        anger_dict[team] = average_sentiment(team, 'Anger')

    # sort dicts by value
    joy_ranking = sorted(joy_dict.items(), key=lambda x:x[1], reverse=True)
    sadness_ranking = sorted(sadness_dict.items(), key=lambda x:x[1], reverse=True)
    anger_ranking = sorted(anger_dict.items(), key=lambda x:x[1], reverse=True)

    # display results
    print "Teams ranked by tweet joy:"
    for team in joy_ranking:
        print str(team[0]) + ' ' + str(team[1])
    print

    print "Teams ranked by tweet sadness:"
    for team in sadness_ranking:
        print str(team[0]) + ' ' + str(team[1])
    print

    print "Teams ranked by tweet anger:"
    for team in anger_ranking:
        print str(team[0]) + ' ' + str(team[1])
    print

# parse through JSON to get average sentiment data
def average_sentiment(team, sentiment):
    with open('./sentiment_data/tweet_data.json', 'r') as f:
        data = json.load(f)

    sentiment_sum = 0
    tweet_count = 0
    for tweet in data:
        if (tweet['Team'] == team):
            tweet_count += 1
            if (tweet['Sentiment'].has_key(sentiment)):
                sentiment_sum += tweet['Sentiment'][sentiment]

    return 1.0 * sentiment_sum / tweet_count

if __name__ == '__main__':
    sentiment_ranks()
