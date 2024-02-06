def min_max_and_sum_values(sequence):
    values = list(map(int,sequence.split()))
    min_value = min(values)
    max_value = max(values)
    sum_value = sum(values)
    return min_value, max_value, sum_value

sequence_of_values = input()
min_val, max_val, sum_val = min_max_and_sum_values(sequence_of_values)
print('The minimum number is', min_val)
print('The maximum number is', max_val)
print('The sum number is:', sum_val)

