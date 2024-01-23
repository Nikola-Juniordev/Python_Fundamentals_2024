key = int(input())
num_of_lines = int(input())
for i in range(num_of_lines):
    letter = input()
    code = (ord(letter) + key)
    print(chr(code), end='')



