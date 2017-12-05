from matplotlib import pyplot as plt
import json
import collections

def load_sentiment_scores():
    with open('./sentiment_data/history_sentiments.json', 'r') as f:
        string = f.read()
    sentiment_data = json.loads(string)
    return sentiment_data

def filename_to_name(filename):
    filename = filename.replace('.txt', '')
    filename = filename.replace('_', ' ')
    l = filename.split(' ')
    return l[-1]


def main():
    data = load_sentiment_scores()
    teams = []
    scores = []
    for team in data:
        teams.append(filename_to_name(team['team']))
        try:
            scores.append(float(team['sadness']))
        except:
            scores.append(0.0)
    xs = [i + 0.1 for i, _ in enumerate(teams)]
    plt.bar(xs, scores, .8)
    plt.xticks([i + .1 for i, _ in enumerate(teams)], teams, rotation='vertical')
    axes = plt.gca()
    plt.title("Sadness Scores")
    plt.xlabel('Team')
    plt.ylabel('Score')
    plt.show()


main()
