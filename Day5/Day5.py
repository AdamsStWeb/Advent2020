with open("Input.txt") as f:
    lines = f.readlines() 
    max_seat = 0
    
    for line in lines:
        x, y = '',''
        seat = 0
        for i in range(0,7):
            if line[i] == 'F':
                y = y + '0'
            else:
                y = y + '1'

        for i in range(7,10):
            if line[i] == 'L':
                x = x + '0'
            else:
                x = x + '1'
    
        seat = (int(y,2) * 8) + int(x,2)
    
        if seat > max_seat: max_seat = seat

print(max_seat)    


