guide_win = {"A": "Y", "B": "Z", "C": "X"}
guide_draw = {"A": "X", "B": "Y", "C": "Z"}
points = {"X": 1, "Y": 2, "Z": 3}
points_win, points_draw = 6, 3

with open("in.txt", "r") as file:
    rounds = [tuple(line.strip().split()) for line in file]

total_score = 0
for round in rounds:
    total_score += points[round[1]]

    if round[1] == guide_win[round[0]]:
        total_score += points_win
    if round[1] == guide_draw[round[0]]:
        total_score += points_draw
print(total_score)