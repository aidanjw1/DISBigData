import json
import csv

def load_sentiment_scores():
    with open('./sentiment_data/history_sentiments.json', 'r') as f:
        string = f.read()
    sentiment_data = json.loads(string)
    return sentiment_data

def rank_scores(sentiment):
    scores = load_sentiment_scores()
    rankings = [(data[sentiment], data['team']) for data in scores]
    rankings.sort(reverse = True)
    return rankings

def write_to_csv(data, filename):
    with open('./sentiment_data/' + filename, 'w') as f:
        fieldnames = ['Team', 'Score']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({'Team': item[1], 'Score': item[0]})


def main():
    joys = rank_scores('joy')
    sads = rank_scores('sadness')

    write_to_csv(joys, 'joy_rankings.csv')
    write_to_csv(sads, 'sadness_rankings.csv')

main()
