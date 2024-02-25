initial_energy = int(input())
battles_won_counter = 0

while True:
    distance = input()
    if distance == 'End of battle':
        print(f"Won battles: {battles_won_counter}. Energy left: {initial_energy}" )
        break
    elif initial_energy >= int(distance):
        battles_won_counter += 1
        initial_energy -= int(distance)
        if battles_won_counter % 3 == 0:
            initial_energy += battles_won_counter
    elif initial_energy < int(distance):
        print (f"Not enough energy! Game ends with {battles_won_counter} won battles and {initial_energy} energy")
        break

