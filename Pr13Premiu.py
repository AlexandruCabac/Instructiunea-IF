x=int(input())
if(x<1 or x>100):
    print("Error")
elif(x%4==0):
    print("Tricou de culoare neagră")
elif(x%4==1):
    print("Tricou de culoare albă")
elif(x%4==2):
    print("Tricou de culoare roșie")
else:
    print("Tricou de culoare albastră")
