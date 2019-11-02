import re
cytat = 'To be, or not to be, that is the question'
samogłoski = re.findall('a|e|i|o|u', cytat)

print(f'Liczba samogłosek to:', len(samogłoski))