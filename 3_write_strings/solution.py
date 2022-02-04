def write_strings(f, string_list):
    #Writes the number of strings
    write_uint32(f, len(string_list))

    #For each string, writes it as binary data.
    for string in string_list:        
        write_uint32(f, len(string)+1)
        f.write(string.encode())
        f.write(b'\x00')
