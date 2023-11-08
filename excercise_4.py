numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(numbers)

matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

only_home_wins = list(filter(lambda item: item["home_team_result"] == "Win", matches))
print(only_home_wins)
print(len(only_home_wins))
