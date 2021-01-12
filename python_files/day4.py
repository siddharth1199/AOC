import hashlib 

#Part 1
i=0
key = 'yzbqklnj'
result=''
while(True):
    result = hashlib.md5((key+str(i)).encode()).hexdigest()
    if result[:5]=='00000':
        break
    i=i+1

#Part 2
i=0
key = 'yzbqklnj'
result=''
while(True):
    result = hashlib.md5((key+str(i)).encode()).hexdigest()
    if result[:6]=='000000':
        break
    i=i+1
    
print('Value for 6 zeros = ', i)