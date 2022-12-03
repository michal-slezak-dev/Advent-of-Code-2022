sums = []
sum_val = 0
with open("in.txt", "r") as file:
    for line in file:
       if line.strip() != '':
            sum_val += int(line.strip())
       else:
            sum_val = 0
       if sum_val != 0:
            sums.append(sum_val)
print(sum(sorted(sums)[-3:]))