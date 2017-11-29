from WikiData import get_history_text

def main():
    with open('./teams.txt', 'r') as f:
        teams = f.read()
    teams = teams.split('\n')

    for team in teams:
        h = get_history_text(team)
        with open('./history/{0}.txt'.format(team), 'w') as f:
            f.write(h)

main()
