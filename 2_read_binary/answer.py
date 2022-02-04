def read_string(f):
    #read 4-byte
    binary=f.read(4)

    #convert byte data to an integer.
    length = int.from_bytes(binary, "little")

    #read bytes and decode to string
    string = f.read(length-1).decode()

    #skip 1 byte (00)
    f.seek(1,1)
    
    return string

file = "test_string.bin"

f = open(file, "rb")

string=read_string(f)
print("string: "+string)
print("length: {}".format(len(string)))

f.close()