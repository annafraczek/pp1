class arrays(): 
    global sep 
    sep = ','
    @staticmethod 
    def print_in_col(array): 
        for c in array: 
            print(c) 
    @staticmethod 
    def print_split(array):
        for c in range(len(array)-1):
            print(array[c],end = sep)
        print(array[-1])
    @staticmethod 
    def create_array(liczba_elem,wartosc_elem):
        array = []
        for i in range(liczba_elem):
            array.append(wartosc_elem)
        return array
    @staticmethod 
    def create_random_array(liczba_elem,wartosc_od,wartosc_do):
        from random import randrange
        array = []
        for i in range(liczba_elem):
            array.append(randrange(wartosc_od,wartosc_do+1))
        return array
    @staticmethod
    def what_elem(array,wartosc_od,wartosc_do):
        licznik = 0
        for i in array:
            if i>=wartosc_od and i<=wartosc_do:
                licznik +=1
        return licznik
    @staticmethod
    def change_sep(new_sep):
        global sep 
        sep = new_sep


my_array = [4,1,8,7,2] 
arrays.print_in_col(my_array)
arrays.print_split(my_array)

arrays.change_sep(';')
new_array = arrays.create_array(10,4)
arrays.print_split(new_array)

new_random_array = arrays.create_random_array(20,-7,8)
arrays.print_split(new_random_array)

print(arrays.what_elem(new_random_array,-1,1))