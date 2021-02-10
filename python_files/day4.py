import hashlib 

def hash_key_val(s, val, start_point):
    i=start_point
    result=''
    zero_str = '0'*val
    while(True):
        result = hashlib.md5((s+str(i)).encode()).hexdigest()
        if result[:val]==zero_str:
            break
        i=i+1
    return i
    
    
def main():
    s = 'yzbqklnj'
    #s = input('Enter string here (with ""): ')
    part_1 = hash_key_val(s, 5, 0)
    part_2 = hash_key_val(s, 6, part_1)
    print('Part 1', part_1)
    print('Part 2', part_2)
    
if __name__ == "__main__":
    main()
