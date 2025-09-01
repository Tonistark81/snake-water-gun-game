'''
1 = snake
-1 = water
0 = gun

'''
import random

computer = random.choice([1, -1, 0])


youstr = input("Enter your choice:")

youDict = {"s" : 1, "w" :-1, "g" : 0}
reverseDict = {1 : "Snake", -1 :"Water", 0 : "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == 1 and you == -1):
        print("you lose!")
        
    elif(computer == 0 and you == 1):
        print("you lose!")
        
    elif(computer == -1 and you == 0):
        print("you lose!")
        
    elif(computer == -1 and you == 1):
        print("you win!")
        
    elif(computer == 1 and you == 0):
        print("you win!")
        
    elif(computer == 0 and you == -1):
        print("you win")


