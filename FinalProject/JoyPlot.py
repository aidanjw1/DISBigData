from matplotlib import pyplot as plt
import json
import collections

def load_sentiment_scores():
    with open('./sentiment_data/history_sentiments.json', 'r') as f:
        string = f.read()
    sentiment_data = json.loads(string)
    return sentiment_data

def main():
    data = load_sentiment_scores()
    teams = []
    scores = []
    for team in data:
        teams.append(team['team'])
        try:
            scores.append(float(team['Joy']))
        except:
            scores.append(0.0)
    # import matplotlib.pyplot as plt
    # listofnames = ['Al', 'Ca', 'Re', 'Ma', 'Al', 'Ma', 'Ma', 'Re', 'Ca']
    xs = [i + 0.1 for i, _ in enumerate(teams)]
    plt.bar(xs, scores, .8)
    plt.xticks([i + .1 for i, _ in enumerate(teams)], teams, rotation='vertical')
    axes = plt.gca()
    axes.set_ylim([.45,.7])
    plt.show()


main()
