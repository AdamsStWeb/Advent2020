
with open('Day4Input.txt') as f:
    data = f.read()
    data = data.replace('\n\n', '|')
    data = data.replace('\n', ' ')
    entries = data.split('|')
    
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    count = 0
    for entry in entries:
        valid = all(field in entry for field in required)
        count += valid

    print(count)