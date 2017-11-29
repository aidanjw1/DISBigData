import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3



tone_analyzer = ToneAnalyzerV3(
	  username='e85a5f56-71dd-4ad9-86d6-6cd04cdf2986',
	  password='sbf7EgP2TpIb',
	  version='2017-09-26'
	)


def toneAnalyzer(text):
	tone = tone_analyzer.tone(text, tones='emotion',
    content_type='text/plain')
  	prettyTone = json.dumps(tone, indent=2)
  	toneList = tone['document_tone']['tones']
  	print(text)
  	print(prettyTone)

	for tone in toneList:
		print("Tone: ", tone['tone_name'], "Score: " , tone['score'])

def main():
	toneAnalyzer("Lebron James and the cavaliers are playing amazing basketball these last 3 weeks")
	toneAnalyzer("I hate what magic johnson and the Lakers are doing right now with Lonzo Ball")




main()













