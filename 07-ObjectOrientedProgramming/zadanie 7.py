class Student():
    licznik=100000
    kierunek="Informatyka stosowana"
    uniwersytet="UEK Kraków"
    
    def __init__(self,imię):
        self.imię=imię
        self.album=Student.licznik
        Student.licznik+=1
        
    def __str__(self):
        return f'{self.imię}, {Student.licznik}, {Student.kierunek}, {Student.uniwersytet}'

student1=Student("Jan Kowalski")
print(student1)
student2=Student("Adam Nowak")
print(student2)
student3=Student("Ala Kot")
print(student3)