jezyki = ['java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android' ]
wartosci = [61,47,37,32,26,18,14,14,9,7]

def rysujWykres(jezyki, wartosci):
    for i in range(len(jezyki)):
        string = jezyki[i]
        string = string.rjust(15,' ')
        print(string,':', '#'*wartosci[i])

rysujWykres(jezyki, wartosci)