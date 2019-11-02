tablica=[32,16,5,8,24,7]
with open ('C:/Users/Anna/Desktop/pp1/03-FileHandling/tablica.txt','w') as file:
    for x in tablica:
        file.write(str(x)+'\n')