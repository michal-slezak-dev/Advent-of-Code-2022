lowercase_points = {chr(i + 96): i for i in range(1, 27)}
uppercase_points = {chr(i + 38): i for i in range(27, 53)}

with open("in.txt", "r") as file:
    rucksacks = [(''.join(line.strip()[:len(line.strip()) // 2]), ''.join(line.strip()[len(line.strip()) // 2:])) for line in file]

priorities = []
for rucksack in rucksacks:
    for item in rucksack[0]:
        if item in rucksack[1]:
            if item.isupper():
                item = uppercase_points[item]
            else:
                item = lowercase_points[item]

            priorities.append(item)
            break
print(sum(priorities))