number_of_cityes_visited = int(input())
total_profit = 0
cityes_visited = 0

for city in range(number_of_cityes_visited):
    city_name = input()
    cityes_visited += 1
    owners_income = float(input())
    owners_expense = float(input())
    if cityes_visited % 3 == 0:
        owners_expense = owners_expense * 1.5
        city_profit = owners_income - owners_expense
        total_profit += city_profit
        print(f"In {city_name} Burger Bus earned {city_profit:.2f} leva.")
    elif cityes_visited % 5 == 0:
        owners_income = owners_income * 0.90
        city_profit = owners_income - owners_expense
        total_profit += city_profit
        print(f"In {city_name} Burger Bus earned {city_profit:.2f} leva.")
    else:
        city_profit = owners_income - owners_expense
        total_profit += city_profit
        print(f"In {city_name} Burger Bus earned {city_profit:.2f} leva.")


print(f"Burger Bus total profit: {total_profit:.2f} leva.")


