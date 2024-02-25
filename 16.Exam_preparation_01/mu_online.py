def receive_potion(current_health, room, heal_amount):
    room += 1
    heal_needed = 100 - current_health
    if heal_needed > 0:
        actual_heal = min(heal_amount, heal_needed)
        current_health += actual_heal
        print(f"You healed for {actual_heal} hp.")
        print(f"Current health: {current_health} hp.")
    else:
        print("You are already at full health.")
    return current_health, room

def found_chests(initial_bitcoin, room, bitcoins_found):
    room += 1
    initial_bitcoin += bitcoins_found
    print(f"You found {bitcoins_found} bitcoins.")
    return initial_bitcoin, room

def fight_monster(current_health, room, command):
    room += 1
    monster_type = command[0]
    monster_attack = int(command[1])
    current_health -= monster_attack
    if current_health <= 0:
        print(f"You died! Killed by {command[0]}.")
        print(f"Best room: {room}")
        return None, None  # Return None for current_health and room if player dies
    else:
        print(f"You slayed {command[0]}.")
        return current_health, room

def explore_dungeon(dungeon_rooms):
    initial_health = 100
    initial_bitcoin = 0
    current_health = initial_health
    room = 0

    for command in dungeon_rooms:
        command = command.split()
        if command[0] == 'potion':
            current_health, room = receive_potion(current_health, room, int(command[1]))
            if current_health is None:  # Player died
                return
        elif command[0] == 'chest':
            initial_bitcoin, room = found_chests(initial_bitcoin, room, int(command[1]))
        else:
            current_health, room = fight_monster(current_health, room, command)
            if current_health is None:  # Player died
                return

    print("You've made it!")
    print(f'Bitcoins: {initial_bitcoin}')
    print(f'Health: {current_health}')

# Main part of the code
dungeon_rooms_input = input().split('|')
explore_dungeon(dungeon_rooms_input)
