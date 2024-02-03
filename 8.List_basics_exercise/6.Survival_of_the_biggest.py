received_numbers = input().split()
numbers_to_remove = int(input())


received_numbers = list(map(int, received_numbers))

for _ in range(numbers_to_remove):
    if received_numbers:
        min_value = min(received_numbers)
        received_numbers.remove(min_value)

result = ", ".join(map(str, received_numbers))
print(result)


Solution 2:

list_of_ints = input().split()
numbers_to_remove = int(input())
list_of_integers = []
for num in range(0, len(list_of_ints)):
   list_of_ints[num] = int(list_of_ints[num])
   list_of_integers.append(list_of_ints[num])
while numbers_to_remove > 0 and list_of_integers:
   list_of_integers.remove(min(list_of_integers))
   numbers_to_remove -= 1
print(*list_of_integers, sep=', ')