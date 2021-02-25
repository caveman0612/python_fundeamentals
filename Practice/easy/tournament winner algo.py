

def tournamentWinner(competitions, results):
    winner_dict = {}
    for list1, result in zip(competitions, results):
        if result == 1:
            if list1[0] not in winner_dict:
                winner_dict[list1[0]] = 3
            else:
                winner_dict[list1[0]] += 3
        else:
            if list1[1] not in winner_dict:
                winner_dict[list1[1]] = 3
            else:
                winner_dict[list1[1]] += 3
    winner_dict = dict(sorted(winner_dict.items(), key=lambda items: items[1], reverse=True))
    winner = list(winner_dict.keys())[0]
    return winner



competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
# [hometeam, awayteam] + 3 points for winners

results = [0, 0, 1]
# 1 = home team 0 = awayteam

tournamentWinner(competitions, results)