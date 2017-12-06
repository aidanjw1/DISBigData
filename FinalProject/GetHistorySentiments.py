from IBManalysis import toneAnalyzer
from WikiData import get_cleaned_text

import os
import json

team_data = {}
out = []

for name in os.listdir('./history/'):
    sad = 0
    joy = 0
    with open('./history/' + name, 'r') as f:
        hist = f.read()
    # Perform sentiment analysis on fractions of the history text
    # and sum the values for each team
    frac = 6
    for i in range(frac):
        start = int((i / float(frac)) * len(hist))
        end = int((i + 1) / float(frac) * len(hist))
        try:
            tones = toneAnalyzer(hist[start:end], name)
        except:
            continue
        if 'Joy' in tones['Sentiment'].keys():
            joy += tones['Sentiment']['Joy']
        if 'Sadness' in tones['Sentiment'].keys():
            sad += tones['Sentiment']['Sadness']
    team_data = {}
    team_data['team'] = name
    team_data['joy'] = round(joy, 3)
    team_data['sadness'] = round(sad, 3)
    print team_data
    out.append(team_data)

with open('./sentiment_data/history_sentiments.json', 'w') as f:
    json.dump(out, f, indent=4, sort_keys=True)
