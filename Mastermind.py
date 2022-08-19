import random
import time
import sys

print("Welcome to Super MasterMinds game! I will think of a number between [1111,9999] and you will have to guess this number! ")
time.sleep(3)
#Unicode = input("Hey! can you see these as tick, cross, circle? (Y/N)\n ✔️ ❌🟡\n> ").lower()
NoOfTrys = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHow many tries would you like? (Not sure?  just enter 'random' to get a random No of tries!)\n>")
numLen = input("How many numbers do you want your number to be\n>")
SecrectNum = []
SecrectNums = ""
gameend = False


if NoOfTrys.lower() == "random":
    NoOfTrys = random.randrange(3,12)
else:
    NoOfTrys = int(NoOfTrys)
print("You have {} tries! good luck!".format(NoOfTrys))

#if Unicode == "y":
#     Unicodes = ["✔️ ","❌","🟡"]
# else:
#     print("C = Correct\nW = Wrong\nP = Wrong Place")
#     Unicodes = ["C","W","P"]

Unicodes = ["✔️ ","❌","🟡"]

for i in range(int(numLen)):
    SecrectNum.append(random.randint(1,9))
for i in SecrectNum:
    SecrectNums = SecrectNums + str(i)

SecrectNums = int(SecrectNums)
# print(SecrectNums)

counter = 0
while gameend != True:
    UserInput = input("Please enter your guess!\n>")
    try:
        testingss = int(UserInput)
    except:
        print("Thats not a valid number Try again!")
        continue
    if int(UserInput) == SecrectNums:
        print("You won! You got it on your #{} try!".format(counter + 1))
        time.sleep(3)
        gameend = True
    else:
        if len(UserInput) != int(numLen):
            print("Enter a number thats {} digits long!".format(numLen))
            continue
        hint = []
        rotation = 0
        yellowMarkerC = 0
        NumMarkerC = 0
        
        for i in UserInput:
            if int(i) not in SecrectNum: hint.append(Unicodes[1])  
            elif int(i) == SecrectNum[rotation]: hint.append(Unicodes[0]) 
            elif int(i) in SecrectNum: hint.append(Unicodes[2]); yellowMarkerC += 1
            else: hint.append(Unicodes[1])
            rotation += 1
        hintF = ""
        for i in hint:
            hintF = hintF + str(i)
        print(f"Thats not right, {hintF}")


    
    if counter == NoOfTrys:
        print("Thats all your tries! the no was: {}".format(SecrectNums))
        time.sleep(3)
        sys.exit()
    counter += 1

    
sys.exit()


