def take_odd(password):
    new_password = password[1::2]
    print(new_password)
    return new_password

def cut(password, index, length):
    index = int(index)
    length = int(length)
    substring = password[index:index+length]
    password = password.replace(substring, '', 1)
    print(password)
    return password

def substitute(password, substring, substitute):
    if substring in password:
        password = password.replace(substring, substitute)
        print(password)
        return password
    else:
        print("Nothing to replace!")
        return password

def password_reset(password, commands):
    for command in commands:
        if command[0] == "TakeOdd":
            password = take_odd(password)
        elif command[0] == "Cut":
            password = cut(password, command[1], command[2])
        elif command[0] == "Substitute":
            password = substitute(password, command[1], command[2])
        elif command[0] == "Done":
            break
    print("Your password is:", password)


password = input()
commands = []
while True:
    command = input().split()
    if command[0] == "Done":
        break
    commands.append(command)

password_reset(password, commands)


