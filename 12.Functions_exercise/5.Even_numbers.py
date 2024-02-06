def filter_even_numbers(sequence):
    numbers = map(int, sequence.split())
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    return list(even_numbers)


numbers_sequence = input()
even_numbers_list = filter_even_numbers(numbers_sequence)
print(even_numbers_list)