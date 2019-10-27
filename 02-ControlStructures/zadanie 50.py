FinalList = []
dividedList = []

inputNumber = 230
number = inputNumber

while number != 1:
    _new_number, divided =  divmod(number, 2)
    print("{}|{}".format(number, divided))
    number = _new_number
    FinalList.append(divided)
    dividedList.append(number)

if number == 0:
    print('0|0')
    FinalList.append(divided)
    dividedList .append(0)
else:
    print('1|1')
    FinalList.append(1)
    dividedList.append(1)

#print(FinalList[::-1]) # should match with the `bin` result
#print(dividedList)

print(inputNumber, "w wyrażeniu binarnym to:", FinalList[::-1])