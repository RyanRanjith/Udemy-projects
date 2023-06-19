print("welcome to love calculator")
user1=input("enter your name")
user2=input("enter your name")

check1 = user1.lower()
check2 = user2.lower()
ruserf = check1 + check2
final1=ruserf.count("t")
final2=ruserf.count("r")
final3=ruserf.count("u")
final4=ruserf.count("e")
final5=ruserf.count("l")
final6=ruserf.count("o")
final7=ruserf.count("v")
final8=ruserf.count("e")

final9 = final1 + final2 + final3 + final4

final10 = final5 + final6 + final7 + final8

final11 = str(final9) + str(final10)
final12 = int(final11)

if final12 < 10 or final12 > 90:
 print(f"Your score is {final12} , you go together like coke and mentos ")
 
elif final12 <= 40:
    print(f"Your score is{final12} you are alright together")
    
elif final12 <= 50:
    print(f"Your score is {final12} you are alright together")
    
    
else:
    print(f"your score is {final12}")



