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
    sentences = hist.split('.')
    for i in range(len(sentences)/100):
        group = ""
        for j in range(100):
            group += sentences[j + i * 100]
        tones = toneAnalyzer(group, name)
        print tones.keys()
        # if 'Sadness' in tones.keys():
        #     sad += 1
        # if 'Joy' in tones.keys():
        #     joy += 1
        # team_data = {}
        # team_data['team'] = name
        # team_data['joy'] = joy
        # team_data['sadness'] = sad
        # out.append(team_data)
        # i += 1
        # print i
    print 'finished sentiment: ' + name


# for team in team_data.keys():
#     team_tones = {}
#     team_tones['team'] = team
#     for tone in team_data[team]:
#         team_tones[tone['tone_name']] = str(tone['score'])
#     out.append(team_tones)
#     print 'json added: ' + team

with open('./sentiment_data/history_sentiments.json', 'w') as f:
    json.dump(out, f)
