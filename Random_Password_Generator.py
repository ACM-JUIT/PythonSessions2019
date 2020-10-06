import random

def password(size):
   symbol =["$", "@", "#", "%"]
   uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W' , 'X', 'Y', 'Z']
   lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w' , 'x', 'y', 'z']
   num = ['0','1','2','3','4','5','6','7','8','9']



   spChar = [random.choice(symbol) for char in range(size)]
   low_al = [random.choice(lowercase) for low in range(size)]
   up_al = [random.choice(uppercase) for upper in range(size)]
   n = [random.choice(num) for i in range(size)]
   gen_pass = spChar + low_al + up_al + n
   gen_pass = [random.choice(gen_pass) for value in range(size)]

#the generated pass is generated
   return gen_pass


size = int(input("Enter the desired length of the password: "))
ans = password(size)
print(ans)
