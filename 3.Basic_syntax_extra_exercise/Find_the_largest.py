number_input = [n for n in input()]
n = len(number_input)

for i in range(n):
    for j in range(0, n - i - 1):
        if number_input[j] < number_input[j + 1]:

            number_input[j], number_input[j + 1] = number_input[j + 1], number_input[j]

sorted_number = ''.join(number_input)

print(sorted_number)

