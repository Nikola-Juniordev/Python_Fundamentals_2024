inventory = []


def command_collect(item):
    if item not in inventory:
        inventory.append(item)


def command_drop(item):
    if item in inventory:
        inventory.remove(item)


def command_combine(command):
    old_item, new_item = command.split(':')
    if old_item in inventory:
        index = inventory.index(old_item)
        inventory.insert(index + 1, new_item)


def command_renew(item):
    if item in inventory:
        inventory.remove(item)
        inventory.append(item)


journal = input().split(', ')

while True:
    command = input()
    if command == 'Craft!':
        break

    action, item = command.split(' - ')

    if action == 'Collect':
        command_collect(item)
    elif action == 'Drop':
        command_drop(item)
    elif action == 'Combine Items':
        command_combine(item)
    elif action == 'Renew':
        command_renew(item)

print(', '.join(inventory))
