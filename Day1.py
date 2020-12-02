#Day1 Advent
with open("Day1Input.txt") as f:
    numbers = f.readlines()
numbers = [x.strip() for x in numbers] 

#part 1
flag = False
for i in numbers:
    for j in numbers:
        if int(i) + int(j) == 2020:
            print(int(i) * int(j))
            flag = True
            break
    if flag == True: break

#part 2
flag = False
for i in numbers:
    for j in numbers:
        for k in numbers:
            if int(i) + int(j) + int(k) == 2020:
                print(int(i) * int(j) * int(k))
                flag = True
                break
        if flag == True: break    
    if flag == True: break            
        
