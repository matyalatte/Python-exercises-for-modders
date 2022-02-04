'''
We need to read binary data.
So, you should understand how to handle it.

Exercise2 Read Binary

    We want to read string data as binary.
    The format is as follows.

    * First 4-byte is the length of strings plus 1.
    * The last 1-byte is 0.
    * The rest of the binary data is a string as utf-8.

    For example,
    "hello!" will be represented in the format as "07 00 00 00 68 65 6C 6C 6F 21 00".
    "dog" will be "04 00 00 00 64 6F 67 00".
    "Bruh" will be "05 00 00 00 42 72 75 68 00".

    Write the function "read_string(f)" to read the string data.
    When you run this program, you have to see the following messages.

    string: You got it!
    length: 11
'''

def read_string(f):
    #write code here!

file = "test_string.bin"

f = open(file, "rb")

string=read_string(f)
print("string: "+string)
print("length: {}".format(len(string)))

f.close()