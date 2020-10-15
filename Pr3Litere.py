lit=input()
Voc=['a','A', 'â','Â', 'ă','Ă', 'e','E','i','I','î','Î', 'o','O','u','U','y','Y',]
Con=['b','B','c','C','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','ș','Ș','t','T','ț','Ț','v','V','w','W','x','X','z','Z']
if(lit in Voc):
    print("Vocală")
elif(lit in Con):
    print("Consoană")
else:
    print("NU e literă")
