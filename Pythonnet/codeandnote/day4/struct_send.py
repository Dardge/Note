from socket import *
import struct 

fmt = 'i32sif'
ADDR = ('127.0.0.1',8888)

s = socket(AF_INET,SOCK_DGRAM)

while True:
    print("\n*********************")
    id = int(input("ID:"))
    name = input("Name:")
    age = int(input("Age:"))
    score = float(input("Score:"))

    data = struct.pack(fmt,id,\
        name.encode(),age,score)
    s.sendto(data,ADDR)

s.close()
