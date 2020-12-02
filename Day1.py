
with open("Day1Input.txt") as f:
    numbers = f.readlines()
numbers = [x.strip() for x in numbers] 

#part 1
for i in range(len(numbers)):
    x = int(numbers[i])
    for j in range(len(numbers)):
        y = int(numbers[j])
        if x + y == 2020:
            print(x * y)
    
#part 2
for i in range(len(numbers)):
    x = int(numbers[i])
    for j in range(len(numbers)):
        y = int(numbers[j])
        for k in range(len(numbers)):
            z = int(numbers[k])
            if x + y + z == 2020:
                print(x * y * z)
                
        