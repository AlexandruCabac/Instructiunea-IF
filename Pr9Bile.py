a1=int(input("albe mari"))
a2=int(input("albe mici"))
b1=int(input("roșii mari"))
b2=int(input("roșii mici"))
c1=int(input("verzi mari"))
c2=int(input("verzi mici"))
print("Sunt în total",a1+a2+b1+b2+c1+c2,"bile")
if(a1+b1+c1>a2+b2+c2):
    print("Mari:",a1+b1+c1,"bile")
elif(a1+b1+c1<a2+b2+c2):
    print("Mici:",a2+b2+c2,"bile")
else:
    print("Este același nr. de bile mari și mici:",a1+b1+c1)
v=max(a1+a2,b1+b2,c1+c2)
if(a2==v):
    print("Albe:",a1+a2,"bile")
if(b2==v):
    print("Roșii:",b1+b2,"bile")
if(c1+c2==v):
    print("Verzi:",c1+c2,"bile")