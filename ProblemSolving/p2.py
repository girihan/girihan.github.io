
while True:
    bit_string = input()
    if bit_string == '#': break
    bit_list = [ int(s) for s in bit_string if ord(s) - ord('0') <= 9 ]
    isOdd = bit_list.count(1) % 2
    print(bit_string[:-1], end='')
    if bit_string[-1] == 'e': #even
        print(1 if isOdd else 0)
    else: # odd
        print(0 if isOdd else 1)
