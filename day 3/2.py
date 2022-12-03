def get_most_common(rucksack):
    for item in rucksack[0]:
        if item in rucksack[1]:
            return item

lowercase_points = {chr(i + 96): i for i in range(1, 27)}
uppercase_points = {chr(i + 38): i for i in range(27, 53)}

with open("in.txt", "r") as file:
    rucksacks = [line.strip() for line in file]

badges_priorities = []
for i in range(2, len(rucksacks), 3):
    for item in rucksacks[i - 2]:
        if item in rucksacks[i - 1] and item in rucksacks[i]:
            if item.isupper():
                item = uppercase_points[item]
            else:
                item = lowercase_points[item]

            badges_priorities.append(item)
            break
print(sum(badges_priorities))