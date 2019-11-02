import re

with open('C:/Users/Anna/Desktop/pp1/03-FileHandling/land.txt', 'r') as file:
    data = file.read().replace('\n', '')

print(sum([int(d) for d in re.findall("\d{1}", data)]))