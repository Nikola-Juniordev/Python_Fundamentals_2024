event = input()
number_of_coffees = 0
while event != "END":
    if event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        number_of_coffees += 2
    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        number_of_coffees += 1
    event = input()
if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)