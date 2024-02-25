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
        inventory.insert(index + 1, new_item.strip())  # Strip to remove any leading/trailing whitespace

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
        command_collect(item.strip())  # Strip to remove any leading/trailing whitespace
    elif action == 'Drop':
        command_drop(item.strip())  # Strip to remove any leading/trailing whitespace
    elif action == 'Combine Items':
        command_combine(item.strip())  # Strip to remove any leading/trailing whitespace
    elif action == 'Renew':
        command_renew(item.strip())  # Strip to remove any leading/trailing whitespace

print(', '.join(inventory))
