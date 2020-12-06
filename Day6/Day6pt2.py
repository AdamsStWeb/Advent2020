from collections import Counter

with open('input.txt') as f:
    data = f.read()
    data = data.replace('\n\n', '|')
    data = data.replace('\n', ',')
    lines = data.split('|')

    yes_sum = 0
    for line in lines:
        a = dict(Counter(line))
        members = a.get(',')
        if members != None:
            members = int(members) + 1
        else:
            members = 1
        for i in a:
            if int(a.get(i)) == members:
                yes_sum += 1
print(yes_sum)