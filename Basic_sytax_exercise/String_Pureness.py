n = int(input())
flag = 0
for i in range(n):
    word = input()
    for l in range(len(word)):
        if(word[l] == "," or word[l] == "." or word[l] == "_"):
            flag = 1
            break
    if flag > 0:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")

