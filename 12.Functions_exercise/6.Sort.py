def sorted_list_of_numbers(sequence):
    numbers = map(int,sequence.split())
    return list(sorted(numbers))

sequence_of_numbers = input()

print(sorted_list_of_numbers(sequence_of_numbers))