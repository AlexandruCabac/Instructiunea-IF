import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if(a==0 and b==0 and c==0):
    print("S=R, orice x")
elif(a==0 and b==0 and c!=0):
    print("S=Vid, nu are soluții")
elif(a==0 and b!=0):
    print("S={",-(c/b),"}")
elif(a>0 and b==0 and c<0):
    print("S={",-math.sqrt(-(c/a)),';',math.sqrt(-(c/a)),"}")
elif(a<0 and b==0 and c>0):
    print("S={",-math.sqrt(-(c/a)),';',math.sqrt(-(c/a)),"}")
elif(a<0 and b==0 and c<0):
    print("S=Vid, nu are soluții")
elif(a>0 and b==0 and c>0):
    print("S=Vid, nu are soluții")
else:
    if(a+b+c==0):
        print("S={",1,';',c/a,"}")
    else:
        d=b**2-4*a*c
        if(d<0):
            print("S=Vid, nu are soluții")
        elif(d==0):
            print("S={",-(b/(2*a)),"}")
        else:
            print("S={",(-b-math.sqrt(d))/(2*a),';',(-b+math.sqrt(d))/(2*a),"}")