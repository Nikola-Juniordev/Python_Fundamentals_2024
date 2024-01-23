from math import ceil
num_of_people = int(input())
elevator_capacity = int(input())
num_of_courses = ceil(num_of_people / elevator_capacity)
print(num_of_courses)
