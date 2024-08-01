
## The Perfect Guess

import random
n = random.randint(1,100)

a = -1
gusess = 1

while(a != n):

    a = int(input("Guses the number : "))

    if(a>n):

        print("Lower Number Please : ")
        gusess += 1

    elif(a<n):
        print("Higher Number Please : ")
        gusess += 1

print(F"You have guess the number {n} correctly in {gusess} attempts")