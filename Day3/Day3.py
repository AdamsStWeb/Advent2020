with open("Day3Input.txt") as f:
    data = f.readlines() 
data = [x.strip() for x in data]

def trees(data, down, over):
    tree = '#'
    count = 0
    x = 0
    
    for i in range(0,len(data), down):
        if  data[i][x] == tree:
            count = count + 1
        x = x + over
        if x >= len(data[i]):
            y = x - len(data[i])
            x = 0
            x = x + y
    return(count)
#part1
trees2 = trees(data,1,3)
#part 2
trees1 = trees(data,1,1)
trees3 = trees(data,1,5)
trees4 = trees(data,1,7)
trees5 = trees(data,2,1)

product = trees1 * trees2 * trees3 * trees4 * trees5
print(product)

