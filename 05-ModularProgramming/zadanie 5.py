wynagrodzenie=[21600, 4350, 3920, 5590, 3250, 4010]

from statistics import mean
śr_arytm=mean(wynagrodzenie)
print(f'Średnia arytmetyczna wynagrodzeń wynosi {śr_arytm}')

from statistics import median
mediana=median(wynagrodzenie)
print(f'Mediana wynagrodzeń wynosi {mediana}')

from statistics import stdev
odch_standard=stdev(wynagrodzenie)
print(f'Odchylenie standardowe wynosi {odch_standard}')