string_of_numbers = input().split()

def command_add(string_of_numbers, value):
    string_of_numbers.append(value)

def command_remove(string_of_numbers, value):
    if value in string_of_numbers:
        string_of_numbers.remove(value)

def command_replace(string_of_numbers, value, replacement):
    if value in string_of_numbers:
        index = string_of_numbers.index(value)
        string_of_numbers[index] = replacement

def command_collapse(string_of_numbers, value):
    string_of_numbers = [num for num in string_of_numbers if int(num) >= value]
    return string_of_numbers

while True:
    command = input().split()
    action = command[0]

    if action == 'Add':
        command_add(string_of_numbers, command[1])
    elif action == 'Remove':
        command_remove(string_of_numbers, command[1])
    elif action == 'Replace':
        command_replace(string_of_numbers, command[1], command[2])
    elif action == 'Collapse':
        string_of_numbers = command_collapse(string_of_numbers, int(command[1]))
    elif action == 'Finish':
        break

print(' '.join(string_of_numbers))
