import os
import json
from matplotlib import pyplot as plt



team_names = ['@Raptors', '@warriors', '@nuggets',
                   '@okcthunder', '@PelicansNBA', '@dallasmavs',
                   '@hornets', '@Lakers', '@nyknicks',
                   '@Timberwolves', '@LaClippers', '@OrlandoMagic',
                   '@Pacers', '@cavs', '@HoustonRockets',
                   '@BrooklynNets', '@Suns', '@spurs', '@utahjazz',
                   '@celtics', '@ATLHawks', '@DetroitPistons',
                   '@chicagobulls', '@sixers', '@Bucks',
                   '@WashWizards', '@MiamiHEAT', '@memgrizz',
                   '@trailblazers', '@SacramentoKings']

team_dict = {'@Raptors':None, '@warriors': None, '@nuggets': None,
                   '@okcthunder': None, '@PelicansNBA': None, '@dallasmavs': None,
                   '@hornets': None, '@Lakers': None, '@nyknicks': None,
                   '@Timberwolves': None, '@LaClippers': None, '@OrlandoMagic': None,
                   '@Pacers': None, '@cavs': None, '@HoustonRockets': None,
                   '@BrooklynNets': None, '@Suns': None, '@spurs': None, '@utahjazz': None,
                   '@celtics': None, '@ATLHawks': None, '@DetroitPistons': None,
                   '@chicagobulls': None, '@sixers': None, '@Bucks': None,
                   '@WashWizards': None, '@MiamiHEAT': None, '@memgrizz': None,
                   '@trailblazers': None, '@SacramentoKings': None}

team_scores = []


NBA_Rankings = ['@celtics', '@HoustonRockets', '@warriors', '@cavs', '@Raptors', '@spurs', '@DetroitPistons',
                  '@nuggets', '@sixers', '@Timberwolves', '@Bucks', '@trailblazers', '@WashWizards', '@Pacers',
                  '@utahjazz', '@PelicansNBA', '@nyknicks', '@okcthunder', '@MiamiHEAT', '@hornets',
                  '@OrlandoMagic', '@BrooklynNets', '@LaClippers', '@Lakers', '@memgrizz', '@dallasmavs', '@Suns', '@SacramentoKings',
                  '@ATLHawks', '@chicagobulls']

NBA_TopHalf = ['@celtics', '@HoustonRockets', '@warriors', '@cavs', '@Raptors', '@spurs', '@DetroitPistons',
                  '@nuggets', '@sixers', '@Timberwolves', '@Bucks', '@trailblazers', '@WashWizards', '@Pacers',
                  '@utahjazz']

NBA_BottomHalf = ['@celtics', '@HoustonRockets', '@warriors', '@cavs', '@Raptors', '@spurs', '@DetroitPistons',
                  '@nuggets']

NBA_Top8 = ['@celtics', '@HoustonRockets', '@warriors', '@cavs', '@Raptors', '@spurs', '@DetroitPistons',
                  '@nuggets']


NBA_Top20 = ['@celtics', '@HoustonRockets', '@warriors', '@cavs', '@Raptors', '@spurs', '@DetroitPistons',
                  '@nuggets', '@sixers', '@Timberwolves', '@Bucks', '@trailblazers', '@WashWizards', '@Pacers',
                  '@utahjazz', '@PelicansNBA', '@nyknicks', '@okcthunder', '@MiamiHEAT', '@hornets']


def getNumbers(sentiment):
      with open('./sentiment_data/tweet_data.json', 'r') as f:
            data = json.load(f)

      for team in team_names:
            totalJoy = 0
            numJoy = 0
            numTeamTweets = 0
            for tweet in data:
                  if (tweet['Team'] == team):
                        numTeamTweets += 1
                        if (tweet['Sentiment'].has_key(sentiment)):
                              if (tweet['Sentiment'][sentiment]):
                                    numJoy += 1
            joyPercentage = (1.0 * numJoy / numTeamTweets)
            tup = (team, joyPercentage)
            team_scores.append(tup)

      sorted_data = sorted(team_scores, key=lambda tup: tup[1])
      print (sentiment)
      print (sorted_data)
      Analyze(sentiment,sorted_data)
      #PlotHistoryScore(sentiment, sorted_data)
     
def Analyze(sentiment,sorted_data):
      counter = 0
      teams = [team[0] for team in sorted_data[:20]]
      print (teams)
      for team in teams:
            if (team in NBA_Top20):
                  counter += 1
      print ((counter/20.0)*100)


def PlotHistoryScore(sentiment, sorted_data):

      teams = [team[0] for team in sorted_data]
      scores = [team[1] for team in sorted_data]
      xs = [i + 0.1 for i, _ in enumerate(teams)]
      plt.bar(xs, scores, .8)
      plt.xticks([i + .1 for i, _ in enumerate(teams)], teams, rotation='vertical')
      axes = plt.gca()
      plt.title(sentiment.capitalize() + " Tweet Percentage Scores")
      plt.xlabel('Team')
      plt.ylabel('Score')
      plt.show()


getNumbers("Sadness")
#print (team_dict)