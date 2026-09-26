def characteristic(num_string):
    num = 0
    has_sign = False
    has_dot = False
    has_digits = False
    length = len(num_string)

    if length == 0:
        return (False, 0)
    
    for i in range(length):
        # must finish scan to make sure input is correct or not 
        ch = num_string[i]
        # handle dot 
        if ch == '.':
            # first index or last index or duplicate 
            if i == 0 or i == length - 1 or has_dot: 
                return (False, 0)
            has_dot = True
            continue
        # handle non-number char 
        elif ch < '0' or ch > '9':
            if ch == '-':
                # index != 0 or duplicate 
                if i > 0 or has_sign: 
                    return (False, 0)
                has_sign = True
                continue
            # other illegal char 
            return (False, 0)
        else:
            # handle number  
            if not has_dot:           
                num = num * 10 + int(ch)
            has_digits = True

    if not has_digits:
        # "."
        return (False, 0)
    
    if  has_sign:
        return (True, -num)
    else:
        return (True, num)

def mantissa(num_string):
    numerator = 0
    denominator = 1
    has_sign = False
    has_dot = False
    has_digits = False
    length =  len(num_string)

    if length == 0:
        return (False, 0, 0)
    
    for i in range(0, length):
        ch = num_string[i]
        # handle dot 
        if ch == '.':
            if i == 0 or i == length - 1 or has_dot:
                return (False, 0 ,0)
            has_dot = True
            continue
        # handle non-number char 
        elif ch < '0' or ch > '9':
            if ch == '-':
                if i != 0 or has_sign: 
                    #1- or  --1
                    return (False, 0, 0)
                has_sign = True
                continue
            # other illegal char 
            return (False, 0, 0)
        # handle number 
        elif ch >= '0' and ch  <= '9':
            has_digits = True
            if has_dot:
                numerator = numerator * 10 + int(ch)
                denominator *= 10

    if not has_digits or not has_dot:
        # "."   "123"
        return (False, 0, 0)
    
    return (True, numerator, denominator)

                     