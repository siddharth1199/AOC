import hashlib 

def hash_key_val(s, val):
    i=0
    result=''
    zero_str = '0'*val
    while(True):
        result = hashlib.md5((s+str(i)).encode()).hexdigest()
        if result[:val]==zero_str:
            break
        i=i+1
    return i
    
    
def main():
    #s = 'yzbqklnj'
    s = input('Enter string here (with ""): ')
    print('Part 1', hash_key_val(s, 5))
    print('Part 2', hash_key_val(s, 6))
    
if __name__ == "__main__":
    main()