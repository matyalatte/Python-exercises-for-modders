'''
Exercise.4 Read Objects

    We want to read the list of 3d vectors from binary files.
    The format is as follows.

    * First 4-byte is the number of vectors.
    * The rest of the binary data is the list of vectors.
    * A vector is written as 3 float numbers.
    * A float number is written as 32-bit (4-byte) data.

    For example,
    
    Let v1=(1, 0, 1).
    [v1] will be represented in the format as
    "01 00 00 00 00 00 80 3f 00 00 00 00 00 00 80 3f".
    ("00 00 80 3f" is 1.0 as 32-bit float.)

    Let v2=(0.5, 1, 1), and v3=(0, 0, -1).
    [v2, v3] will be
    "02 00 00 00 00 00 00 3f 00 00 80 3f 00 00 80 3f 00 00 00 00 00 00 00 00 00 00 80 bf".
    ("00 00 00 3f"=0.5, "00 00 80 bf"=-1.0.)

    I implemented Vector class.
    You can read a vector object like this.
    vector = Vector.read(f)
'''
import struct

def read_float32(f):#Reads a 32-bit (4-byte) float
    bin=f.read(4)
    return struct.unpack('<f', bin)[0]

def write_float32(f, x):#Writes a float as 32-bit
    bin = struct.pack('<f', x)
    f.write(bin)

def read_uint32(f):#Reads a 32-bit integer
    bin=f.read(4)
    return int.from_bytes(bin, "little")

class Vector:
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def read(f):
        x= read_float32(f)
        y= read_float32(f)
        z= read_float32(f)
        return Vector(x, y, z)

    def write(f, vector):
        write_float32(f, vector.x)
        write_float32(f, vector.y)
        write_float32(f, vector.z)

'''
    Write the "read_vector_list(f)" function to read the list of vectors.
    When you run this program, you have to see the following messages.

    (1.0, 0.25, -1.0)
    (-1.0, 2.0, -0.5)
    (0.5, 0.5, -1.0)
'''

def read_vector_list(f):
    vector_list=[]
    #fill here!

    return vector_list


#Don't edit below.
file = "test_vectors.bin"

f = open(file, "rb")
vector_list = read_vector_list(f)
f.close()

for v in vector_list:
    print("({}, {}, {})".format(v.x, v.y, v.z))