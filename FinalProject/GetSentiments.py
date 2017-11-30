from IBManalysis import toneAnalyzer
from WikiData import get_cleaned_text

import os
import json

team_data = {}
out = []

for name in os.listdir('./history/'):
    with open('./history/' + name, 'r') as f:
        hist = f.read()
    tones = toneAnalyzer(hist, name)
    team_data[name] = tones
    print 'finished sentiment: ' + name

for team in team_data.keys():
    team_tones = {}
    team_tones['team'] = team
    for tone in team_data[team]:
        team_tones[tone['tone_name']] = str(tone['score'])
    out.append(team_tones)
    print 'json added: ' + team

with open('./sentiment_data/history_sentiments.json', 'w') as f:
    json.dump(out, f)
