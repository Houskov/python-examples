def nDigitBinary(number, n, k):
    if k == n:
        print(number)
    elif k == 1:
        if n == 1:
            print("1")
        else:
            nDigitBinary("1",n,k+1)
    else:        
        nDigitBinary(number + "0",n,k+1)
        nDigitBinary(number + "1",n,k+1)
nDigitBinary("", 5, 1)