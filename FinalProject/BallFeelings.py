import tweepy

consumer_key = 'dv6NWGg4QT8rr979x81KLIsyI'
consumer_secret = 'nRVr5D48SWJhl491PRjMVCxpCUpnUdMPpbgWsDr920Dm6111vc'
access_token = '4855652441-2Ku9RhnqT24ZyjvtyiqrLWUVqbbjNZILhcynw9u'
access_token_secret = 'br2CEMNroCFKYPK8mckafFqhAiRXg6TwW2EhmZZC0riYT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

team_tweets = {'@Raptors':[], '@warriors':[], '@nuggets':[], '@okcthunder':[],
               '@PelicansNBA':[], '@dallasmavs':[], '@hornets':[], '@Lakers':[],
               '@nyknicks':[], '@Timberwolves':[], '@LAClippers':[],
               '@OrlandoMagic':[], '@Pacers':[], '@cavs':[],
               '@HoustonRockets':[], '@BrooklynNets':[], '@Suns':[],
               '@spurs':[], '@utahjazz':[], '@celtics':[], '@ATLHawks':[],
               '@DetroitPistons':[], '@chicagobulls':[], '@sixers':[],
               '@Bucks':[], '@WashWizards':[], '@MiamiHEAT':[], '@memgrizz':[],
               '@trailblazers':[], '@SacramentoKings':[]}

for team in team_tweets.keys():
    f = open('./Tweets/' + team + '.txt', 'a')

    for tweet in tweepy.Cursor(api.search, q=team, lang='en', count=100).items(300):
        if not tweet.text[:2] == 'RT':
            f.write(tweet.text.encode('utf-8') + '\n')

    f.close()
