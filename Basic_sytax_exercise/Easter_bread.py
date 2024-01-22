budget = float(input())
price_of_one_kilogram_of_flour = float(input())
bread_loaf_counter = 0
colored_egg_counter = 0
price_of_one_pack_of_eggs = price_of_one_kilogram_of_flour - (price_of_one_kilogram_of_flour * 0.25)
price_of_one_liter_of_milk = price_of_one_kilogram_of_flour + (price_of_one_kilogram_of_flour * 0.25)
price_for_250_mill_of_milk = price_of_one_liter_of_milk - (price_of_one_liter_of_milk * 0.75)
price_for_one_loaf = price_for_250_mill_of_milk + price_of_one_kilogram_of_flour + price_of_one_pack_of_eggs
number_of_loafs_made = budget // price_for_one_loaf
money_left = budget - (number_of_loafs_made * price_for_one_loaf)

while budget > price_for_one_loaf:
    budget -= price_for_one_loaf
    bread_loaf_counter += 1
    colored_egg_counter += 3
    if bread_loaf_counter % 3 == 0:
            colored_egg_counter -= bread_loaf_counter - 2
    if budget < price_for_one_loaf:
        break

print(f"You made {bread_loaf_counter} loaves of Easter bread! Now you have {colored_egg_counter} eggs and {money_left:.2f}BGN left.")