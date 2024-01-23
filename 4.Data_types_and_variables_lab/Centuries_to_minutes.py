num_of_centuries = int(input())
num_of_years = num_of_centuries * 100
num_of_days = int(num_of_years * 365.2422)
num_of_hours = num_of_days * 24
num_of_minutes = num_of_hours * 60
print(f'{num_of_centuries} centuries = {num_of_years} years = {num_of_days} days = {num_of_hours} hours = {num_of_minutes} minutes')
