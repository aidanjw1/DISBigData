import requests as rq
import json
from bs4 import BeautifulSoup

teams = ['ATL', 'BOS', 'NJN', 'CHA', 'CHI', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU',
'IND', 'LAC', 'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOH', 'NYK', 'OKC', 'ORL', 'PHI',
'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']

def get_html(team):
    url = "https://www.basketball-reference.com/teams/{0}/stats_basic_totals.html".format(
        team)
    d = rq.get(url).text
    return d

def get_winning_pct(html, team):
    wins = 0
    losses = 0
    soup = BeautifulSoup(html)
    rows = soup.find_all('tr')
    for row in rows:
        try:
            wins += int(row.find('td', attrs={'data-stat':'wins'}).text)
            losses += int(row.find('td', attrs={'data-stat':'losses'}).text)
        except:
            continue
    print team
    return (float(wins)/ (wins + losses))


if __name__ == "__main__":
    winning_pct_data = {}
    data = []
    for team in teams:
        html = get_html(team)
        team_pct = get_winning_pct(html, team)
        winning_pct_data[team_pct] = team

    with open('./sentiment_data/winning_pcts.json', 'w') as f:
        json.dump(winning_pct_data, f, indent=4, sort_keys=True)
