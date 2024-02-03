def plan_gifts(gifts_input, commands):
    gifts = gifts_input.split()

    for command in commands:
        tokens = command.split()
        action = tokens[0]

        if action == "OutOfStock":
            gift_to_remove = tokens[1]
            gifts = ["None" if gift == gift_to_remove else gift for gift in gifts]

        elif action == "Required":
            gift_to_replace = tokens[1]
            index = int(tokens[2])
            if 0 <= index < len(gifts):
                gifts[index] = gift_to_replace

        elif action == "JustInCase":
            gifts[-1] = tokens[1]

    filtered_gifts = [gift for gift in gifts if gift != "None"]
    result = " ".join(filtered_gifts)
    return result

if __name__ == "__main__":
    gifts_input = input()
    commands = []

    while True:
        command = input()
        if command == "No Money":
            break
        commands.append(command)

    result = plan_gifts(gifts_input, commands)
    print(result)

solution 2 :
ist_of_gifts = input().split()
command = input()

while command != "No Money":
    command_list = command.split()
    command_command = command_list[0]
    command_item = command_list[1]

    if command_command == "OutOfStock":
        if command_item in list_of_gifts:
            list_of_gifts = ["None" if x == command_item else x for x in list_of_gifts]
    elif command_command == "Required":
        command_index = int(command_list[2])
        if 0 <= command_index < len(list_of_gifts):
            list_of_gifts[command_index] = command_item
    elif command_command == "JustInCase":
        list_of_gifts[-1] = command_item

    command = input()

list_of_gifts = [x for x in list_of_gifts if x != "None"]
print(" ".join(list_of_gifts))