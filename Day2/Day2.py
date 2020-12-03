with open("Day2Input.txt") as f:
    data = f.readlines() 
data = [x.strip() for x in data] 

#### Part 1
arr = []
for line in data:
    arr.append(line.split(' '))

valid_count = 0

for line in arr:
    pw_range = line[0].split('-')
    min_len = int(pw_range[0])
    max_len = int(pw_range[1])

    letter = line[1]
    letter = letter[0]
    
    count = 0
    pw = line[2]
    
    for i in pw:
        if i == letter:
            count = count + 1
    if count >= min_len and count <= max_len:
        valid_count = valid_count + 1
print(valid_count)

### Part 2
valid_count = 0

for line in arr:
    pw_indexs = line[0].split('-')
    index_1 = int(pw_indexs[0]) - 1
    index_2 = int(pw_indexs[1]) - 1

    letter = line[1]
    letter = letter[0]
    
    pw = line[2]

    if pw[index_1] == letter and pw[index_2] != letter:
        valid_count = valid_count + 1
    if pw[index_1] != letter and pw[index_2] == letter:
        valid_count = valid_count + 1
print(valid_count)