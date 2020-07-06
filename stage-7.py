import random
import re
l=['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
z=random.choice(l)
# print(z)
x=("-"*len(z))
noimp,imp=[],[]
print()
count = 0
d=0
while(count<8):
    print()
    print(x)
    n=input("Input a letter:  ")
    
    if(n.islower() and (len(n)==1)):
        if(n in z):
            if(n in noimp):
                print("You already typed this letter")
        
            else:
                for m in re.finditer(n, z):
                    x = x[:m.start()] + n + x[m.start()+1:]
                noimp.append(n)
        else:              
            if(n in imp):
                print("You already typed this letter")
                
            else:
                print("No such letter in the word")
                count+=1
                imp.append(n)
        if(x == z):
            print(z)
            d=1
            break
         
    else:
        if(len(n)!=1):
            print("You should input a single letter")
        elif(not n.islower()):
            print("It is not an ASCII lowercase letter")
        
if(d==1):
    print("""You guessed the word!
You survived!""")
else:
    print("You are hanged!")
      

# print("You survived!" if n in z "You are hanged!")
