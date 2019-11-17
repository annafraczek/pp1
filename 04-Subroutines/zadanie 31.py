def reverse(tab):
    newtab=[]
    for x in range(0,len(tab)):
        newtab.append(tab[-x-1])
    return newtab
t=[2, 5, 4, 1, 8, 7, 4, 0, 9]
print(reverse(t))