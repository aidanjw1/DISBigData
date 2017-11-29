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
  	print(text)
  	print(prettyTone)

  	tonesToAdd = {}


	for tone in toneList:
		tonesToAdd[tone['tone_name']] = tone['score']

	tweet_dict = {'Team': team, 'Tweet': text, 'Sentiment': tonesToAdd}
	print (tweet_dict)
	twitter_data.append(tweet_dict)


def main():
	toneAnalyzer("Lebron James and the cavaliers are playing amazing basketball these last 3 weeks", "Cavaliers")
	toneAnalyzer("@NBA @Cavs bout time someone tossed king james crybaby flopping ass #racism", "Cavs")
	print (twitter_data)




#main()
