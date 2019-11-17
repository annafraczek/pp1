napis = input("Podaj ciąg znaków który chcesz sprawdzić: ")

def checkString(string):
    UpperList = []
    for i in range(len(string)):
        if string[i].isupper():
            UpperList.append(string[i],)

    print(UpperList)
    return UpperList

sum = 0
forCount = 0
for i in range(len(napis)):
    if napis[i].isupper():
        sum = sum + 1
    forCount = forCount + 1

print(sum == len(checkString(napis)))
print(forCount == len(napis))


upList = checkString(napis)