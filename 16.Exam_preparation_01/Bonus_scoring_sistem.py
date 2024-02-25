import math

# Read input
num_students = int(input())
num_lectures = int(input())
additional_bonus = int(input())

max_bonus = float('-inf')  # Initialize max bonus to negative infinity
max_attendance = 0

# Iterate over each student
for _ in range(num_students):
    student_attendance = int(input())
    total_bonus = (student_attendance / num_lectures) * (5 + additional_bonus)
    total_bonus = math.ceil(total_bonus)  # Round the bonus to the nearest larger number
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendance = student_attendance

# Print the result
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_attendance} lectures.")