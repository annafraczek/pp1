import re
from statistics import mean

komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)

cyfry = [int(i) for i in cyfry]

print('Średnia temperatura dla podanych dni to:' , mean(cyfry))