list_of_items = input().split("|")
budget = int(input())
profit = 0
Clothes = 50.00
Shoes = 35.00
Accessories = 20.50
list_bought_items = []

buying_it = False

splitted_type_price = [item.split("->") for item in list_of_items]

for type_price in splitted_type_price:
    item_type = type_price[0]
    item_price = float(type_price[1])
    if item_type == "Clothes":
        if item_price <= 50.00 and budget >= item_price:
            buying_it = True
            budget -= item_price
            if buying_it:
                new_price_item = item_price * 1.40
                profit += item_price * 0.40
                list_bought_items.append(f"{new_price_item:.2f}")
                buying_it = False
    elif item_type == "Shoes":
        if item_price <= 35.00 and budget >= item_price:
            buying_it = True
            budget -= item_price
            if buying_it:
                new_price_item = item_price * 1.40
                profit += item_price * 0.40
                list_bought_items.append(f"{new_price_item:.2f}")
                buying_it = False
    elif item_type == "Accessories":
        if item_price <= 20.50 and budget >= item_price:
            buying_it = True
            budget -= item_price
            if buying_it:
                new_price_item = item_price * 1.40
                profit += item_price * 0.40
                list_bought_items.append(f"{new_price_item:.2f}")
                buying_it = False
print(" ".join(list_bought_items))
print(f"Profit: {profit:.2f}")
summ_of_them = 0
for item in list_bought_items:
    item_final = float(item)
    summ_of_them += item_final
total_money_made = summ_of_them + budget
if total_money_made >= 150:  # Train Ticket
    print(f"Hello, France!")
else:
    print(f"Not enough money.")