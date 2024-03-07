def isAscending(n: int):

    if n < 0: return False
    if n < 10: return True

    while n >= 10: # n = 123

        d1 = n % 10 # 3 
        n = n // 10 # n = 12
        d2 = n % 10 # 2
        if d2 >= d1:
            return False

    return True