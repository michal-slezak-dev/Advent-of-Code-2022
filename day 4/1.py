with open("in.txt", "r") as file:
    raw_data = [line.strip().split(",") for line in file]
assignments_pairs = [(list(map(int, pair[0].split("-"))), list(map(int, pair[1].split("-")))) for pair in raw_data]
# print(assignments_pairs)

counter = 0
for pair in assignments_pairs:
    if pair[1][0] <= pair[0][0] <= pair[1][1] and pair[1][0] <= pair[0][1] <= pair[1][1] or pair[0][0] <= pair[1][0] <= pair[0][1] and pair[0][0] <= pair[1][1] <= pair[0][1]:
        counter += 1

print(counter)
