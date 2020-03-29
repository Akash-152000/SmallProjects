import random
n=int(input("Enter the length of password u want:"))
specialChar=["!","@","#","$","%","^","&","*"]
capital=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
small=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
num=[1,2,3,4,5,6,7,8,9,0]
bigBoy=[specialChar,capital,small,num]
password=""
for i in range(n):
    j=random.choice(bigBoy)
    k=random.choice(j)
    password=password+str(k)
print(password)
    
    
    
