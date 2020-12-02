#Day1 Advent
with open("Day1Input.txt") as f:
    numbers = f.readlines()
numbers = [x.strip() for x in numbers] 

#part 1
for i in numbers:
    for j in numbers:
        if int(i) + int(j) == 2020:
            print(int(i) * int(j))
    
#part 2
for i in numbers:
    for j in numbers:
        for k in numbers:
            if int(i) + int(j) + int(k) == 2020:
                print(int(i) * int(j) * int(k))
                
        
