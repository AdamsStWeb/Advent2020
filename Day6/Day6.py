with open('input.txt') as f:
    data = f.read()
    data = data.replace('\n\n', '|')
    data = data.replace('\n', ' ')
    lines = data.split('|')

    yes_sum = 0
    for line in lines:
        line = line.replace(' ', '')
        count = len(set(line))
        yes_sum = count + yes_sum
    print(yes_sum)
