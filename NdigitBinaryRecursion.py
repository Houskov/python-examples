def nDigitBinary(n, number= "1"):
    if n == 1:
        print(number)
    else:        
        nDigitBinary(n - 1, number + "0")
        nDigitBinary(n - 1, number + "1")
nDigitBinary(5)