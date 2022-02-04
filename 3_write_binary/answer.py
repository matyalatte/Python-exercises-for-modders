def write_uint32(f, n):#Writes integer n as 4-byte data
    binary = n.to_bytes(4, byteorder="little")
    f.write(binary)

def write_strings(f, string_list):
    #writes the number of strings
    write_uint32(f, len(string_list))

    for string in string_list:
        #for each string, writes it as binary data.
        write_uint32(f, len(string)+1)
        f.write(string.encode())
        f.write(b'\x00')

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