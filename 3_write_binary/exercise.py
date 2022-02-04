'''
We need to write binary data.
So, you should understand how to handle it.

Exercise3 Write Binary
    
    We want to write the list of strings as binary.
    The format is as follows.

    * First 4-byte is the length of the list.
    * For each string, it is written as binary.
        (The format of string is the same as Exercise2.)

    For example,
    ["hello!"] will be represented in the format as
    "01 00 00 00 07 00 00 00 68 65 6C 6C 6F 21 00".

    ["dog", "Bruh"] will be
    "01 00 00 00 04 00 00 00 64 6F 67 00 05 00 00 00 42 72 75 68 00".

    Write the function "write_strings(f, str_list)" to write the list of strings.
    When you run this program, you have to see the following messages.

    Testing...
    Ok!
'''
def write_uint32(f, n):#Writes integer n as 4-byte data
    binary = n.to_bytes(4, byteorder="little")
    f.write(binary)

def write_strings(f, string_list):
    #write code here!

#Don't edit below.
file = "string_list.bin"
string_list=["Text1", "Fire", "You are amazing!", "Based"]

print("Testing...")
with open(file, "wb") as f:
    write_strings(f, string_list)

#compare 2 files
with open(file, "rb") as f:
    binary_actual=f.read()
with open("answer.bin", "rb") as f:
    binary_expected=f.read()
if binary_actual==binary_expected:
    print("Ok!")
else:
    print("Error")
