a=int(input("anul curent"))
b=int(input("luna curentă"))
c=int(input("ziua curentă"))
x=int(input("anul nașterii"))
y=int(input("luna nașterii"))
z=int(input("ziua nașterii"))
if(a<x):
    print("Error")
if(a==x and b<y):
    print("Error")
if(a==x and b==y and c<z):
    print("Error")
v=a-x
if(b<y):
    print(v-1,"ani")
elif(b==y and c<z):
    print(v-1,"ani")
else:
    print(v,"ani")