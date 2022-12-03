max_sum = -1
sum_val = 0
with open("in.txt", "r") as file:
    for line in file:
       if line.strip() != '':
            sum_val += int(line.strip())
       else:
            sum_val = 0

       if sum_val > max_sum:
            max_sum = sum_val
print(max_sum)