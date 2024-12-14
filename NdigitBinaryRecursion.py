def nDigitBinary(number, n, depth):
    if depth == n:
        print(number)
    elif depth == 1:
        nDigitBinary("1", n, depth+1)
    else:        
        nDigitBinary(number + "0", n, depth+1)
        nDigitBinary(number + "1", n, depth+1)
nDigitBinary("", 5, 1)