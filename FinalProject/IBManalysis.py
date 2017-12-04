import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3



tone_analyzer = ToneAnalyzerV3(
	  username='e85a5f56-71dd-4ad9-86d6-6cd04cdf2986',
	  password='sbf7EgP2TpIb',
	  version='2017-09-26'
	)

twitter_data = []


def toneAnalyzer(text, team):
	tone = tone_analyzer.tone(text, tones='emotion',
    content_type='text/plain')
  	prettyTone = json.dumps(tone, indent=2)
  	toneList = tone['document_tone']['tones']
  	tonesToAdd = {}


	for tone in toneList:
		tonesToAdd[tone['tone_name']] = tone['score']

	tweet_dict = {'Team': team, 'Tweet': text, 'Sentiment': tonesToAdd}
	twitter_data.append(tweet_dict)

	return tweet_dict

