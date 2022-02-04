def read_vector_list(f):
    vector_list=[]

    num=read_uint32(f)
    for i in range(num):
        v=Vector.read(f)
        vector_list.append(v)

    return vector_list
