a=int(input("Nr. de găini"))
b=int(input("Nr. de boabe"))
if(b%(a+1)==0):
    print(b//(a+1),"egalitate")
else:
    print("Curcanul primește mai mult cu:",b%(a+1),"boabe")