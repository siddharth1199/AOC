# part 1
i=0
with open('../inputs/day1.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            print ("End of file")
            break
        else:
            if c=='(':
                i=i+1
            else:
                i=i-1
print('floor = ', i)           

# part 2
i=0
j=0
with open('../inputs/day1.txt') as f:
    while True:
        c = f.read(1)
        j=j+1
        if not c:
            print ("End of file")
            break
        else:
            if c=='(':
                i=i+1
            else:
                i=i-1
            if i == -1:
                print('basement loc = ', j)
                break
                