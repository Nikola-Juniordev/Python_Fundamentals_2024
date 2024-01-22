user_age = int(input())

if user_age <= 14:
    print(f'drink toddy')
elif user_age >14 and user_age <=18:
    print(f'drink coke')
elif user_age >18 and user_age <=21:
    print(f'drink beer')
else:
    print(f'drink whisky')