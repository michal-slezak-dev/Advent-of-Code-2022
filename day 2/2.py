# X - lose Y - draw Z - win
guide = {"X": False, "Y": None, "Z": True}  # lose, draw, win
guide_win = {"A": "Y", "B": "Z", "C": "X"}
guide_draw = {"A": "X", "B": "Y", "C": "Z"}
guide_lose = {"A": "Z", "B": "X", "C": "Y"}

points = {"X": 1, "Y": 2, "Z": 3}  # Rock, Paper, Scissors
points_win, points_draw = 6, 3

with open("in.txt", "r") as file:
    rounds = [tuple(line.strip().split()) for line in file]

total_score = 0
for round in rounds:
    if guide[round[1]]:
        total_score += points[guide_win[round[0]]] + points_win
        # print(points[guide_win[round[0]]] + points_win)
    if guide[round[1]] is None:
        total_score += points[guide_draw[round[0]]] + points_draw
        # print(points[guide_draw[round[0]]] + points_draw)
    if guide[round[1]] == False:
        total_score += points[guide_lose[round[0]]]
        # print(points[guide_lose[round[0]]])

print(total_score)