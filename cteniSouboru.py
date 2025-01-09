f = open("/home/ohousar/git/python/python-examples/testfile.txt", "r")
radek = ""
while True:
    radek = f.readline()
    print(radek)
    if radek=="":
        break

