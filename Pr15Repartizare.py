a=int(input())
if(a>125 or a<1):
    print("Error")
elif((a-1)//25==0):
    print("A")
elif((a-1)//25==1):
    print("B")
elif((a-1)//25==2):
    print("C")
elif((a-1)//25==3):
    print("D")
else:
    print("E")