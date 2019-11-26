import time
x = 0
xg = 0
y = 0
yg = 0
EngNum = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
Player1List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Player2List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def CheckInRange():
    global Check
    if CheckDigital >=0 and CheckDigital <= 7:
        Check = True
    else:
        Check = False
    
print("Welcome to the Ta")
time.sleep(0.1)
print("a")
time.sleep(0.2)
print("a")
time.sleep(0.3)
print("a")
time.sleep(0.1)
print("a")
time.sleep(0.2)
print("a")
time.sleep(0.3)
print("a")
time.sleep(0.2)
print("a")
time.sleep(0.1)
print("a")
time.sleep(0.2)
print("a")
time.sleep(0.2)
print("Tank Game")
time.sleep(1)
print("Welcome to the 'Tank Game'!")
time.sleep(1)
print("This is a two player game")
time.sleep(2)
print("So please find your friend to play with you...")

while True:
    print("Are you both ready?")
    YN = input("y/n: ")
    if YN == "yes" or YN == "YES" or YN == "Yes" or YN == "Y" or YN == "y":
        print("Great to know that :) ")
        time.sleep(2)
        print("So let's get STARTED")
        break
    else:
        print("Let me give you both more time to ready, just tell me once you both are READY!")
        time.sleep(2)
        
        continue

print("Let's set a player name for player 1!")
Player1Name = input("Player 1 Name: ")
print("Hello, " + Player1Name + "!")
time.sleep(2)
print("So let's set a player name for player 2!")
Player2Name = input("Player 2 Name: ")
print("Hello, " + Player2Name + "!")
time.sleep(1)
print("Great to know both of your names.")
time.sleep(1)
print("So what are we going to do now?")
time.sleep(1)
print("Both of you need to place 10 tanks on the board")
time.sleep(1)
print("and neither of you should reveal your tank position to each other")
time.sleep(1)
print("Now let's start with " + Player1Name +" first!")
time.sleep(2)
print(Player2Name + ", please TURN your face around, and DON'T LOOK at the screen.")

while x < 10:
    while True:
        time.sleep(1)
        print("Please MAKE SURE " + Player2Name + " is NOT looking at the screen.")
        ShowEngNum = EngNum[x]
        while True:
            print(Player1Name + ", please enter the " + ShowEngNum + " tank in COLUMN from 0-7.")
            Player1C = int(input("The " + ShowEngNum + " tank will be at COLUMN: "))
            CheckDigital = Player1C
            CheckInRange()
            if Check == True:
                print(".")
                break
            else:
                print("You have entered an invaild value, please try again.")
                print(".")
                time.sleep(1)
                continue
            
        while True:
            time.sleep(1)
            print(Player1Name + ", please enter the " + ShowEngNum + " tank in ROW from 0-7.")
            Player1R = int(input("The " + ShowEngNum + " tank will be at ROW: "))
            CheckDigital = Player1R
            CheckInRange()
            if Check == True:
                print(".")
                break
            else:
                print("You have entered an invaild value, please try again.")
                print(".")
                time.sleep(1)
                continue

        Player1CR = str(Player1C) + str(Player1R)
        if Player1CR in Player1List:
            print("There is a tank on the place you want to place already!!!")
            print("Please RE-ENTER...")
            print(".")
            continue
        else:
            break
    
    Player1List[x] = Player1CR
    #print(Player1List)
    print("Sucessful added the " + ShowEngNum + " tank into at column " + str(Player1C) + ", row " + str(Player1R) + ".")

    x = x + 1
    #print(x)

print("Please tell " + Player2Name + " to face here.")
time.sleep(2)
print(Player2Name + ", it is your turn to place the tank!")
time.sleep(2)
print(Player1Name + ", please TURN your face around, and DON'T LOOK at the screen.")

while y < 10:
    while True:
        time.sleep(1)
        print("Please MAKE SURE " + Player1Name + " is NOT looking at the screen.")
        ShowEngNum = EngNum[y]
        while True:
            print(Player2Name + ", please enter the " + ShowEngNum + " tank in COLUMN from 0-7.")
            Player2C = int(input("The " + ShowEngNum + " tank will be at COLUMN: "))
            CheckDigital = Player2C
            CheckInRange()
            if Check == True:
                print(".")
                break
            else:
                print("You have entered an invaild value, please try again.")
                print(".")
                time.sleep(1)
                continue
            
        while True:
            time.sleep(1)
            print(Player2Name + ", please enter the " + ShowEngNum + " tank in ROW from 0-7.")
            Player2R = int(input("The " + ShowEngNum + " tank will be at ROW: "))
            CheckDigital = Player2R
            CheckInRange()
            if Check == True:
                print(".")
                break
            else:
                print("You have entered an invaild value, please try again.")
                print(".")
                time.sleep(1)
                continue

        Player2CR = str(Player2C) + str(Player2R)
        if Player2CR in Player2List:
            print("There is a tank on the place you want to place already!!!")
            print("Please RE-ENTER...")
            print(".")
            continue
        else:
            break
    
    Player2List[y] = Player2CR
    #print(Player2List)
    print("Sucessful added the " + ShowEngNum + " tank into at column " + str(Player2C) + ", row " + str(Player2R) + ".")

    y = y + 1
    #print(y)

print(Player2Name + ", please tell " + Player1Name + " to face here.")
time.sleep(2)
print("Ohhhhh!!!")
print("F")
time.sleep(0.1)
print("i")
time.sleep(0.2)
print("i")
time.sleep(0.3)
print("i")
time.sleep(0.1)
print("i")
time.sleep(0.2)
print("i")
time.sleep(0.3)
print("i")
time.sleep(0.2)
print("i")
time.sleep(0.1)
print("i")
time.sleep(0.2)
print("i")
time.sleep(0.2)
print("Finally...")
time.sleep(0.2)
print("Both of you have finished to set up this 'Tank Game'!")
time.sleep(0.2)
print("So let's get STARTED...")
time.sleep(0.2)
print("Let's start with " + Player1Name + ".")

while True:
    
    #Player1 to Player2
    while True:
        while True:
            print(Player1Name + ", please enter " + Player2Name + "'s tank position at COLUMN from 0-7")
            GPlayer1C2 = int(input(Player2Name + "'s tank position will be at COLUMN: "))
            CheckDigital = GPlayer1C2
            CheckInRange()
            if Check == True:
                break
            else:
                print("You have entered an invaild value, please try again.")
                time.sleep(0.2)
                continue

        while True:
            print(Player1Name + ", please enter " + Player2Name + "'s tank position at ROW from 0-7")
            GPlayer1R2 = int(input(Player2Name + "'s tank position will be at ROW: "))
            CheckDigital = GPlayer1R2
            CheckInRange()
            if Check == True:
                break
            else:
                print("You have entered an invaild value, please try again.")
                time.sleep(0.2)
                continue

        GPlayer1CR2 = str(GPlayer1C2) + str(GPlayer1R2)
        if GPlayer1CR2 in Player2List:
            Player2List.remove(GPlayer1CR2)
            print("Congratulations")
            time.sleep(1)
            print(Player1Name + " have destroyed a tank of " + Player2Name +", at column " + str(GPlayer1C2) + ", row " + str(GPlayer1R2)+ ".")
            time.sleep(1)
            print("So " + Player1Name + " can have one more in this round.")
            print(".")
            xg = xg + 1
            print(xg)
            continue
        else:
            print("Unfortunately...")
            print(Player1Name + " didn't guess it right :(")
            print(".")
            break

    #Player2 to Player1
    while True:
        while True:
            print(Player2Name + ", please enter " + Player1Name + "'s tank position at COLUMN from 0-7")
            GPlayer2C1 = int(input(Player1Name + "'s tank position will be at COLUMN: "))
            CheckDigital = GPlayer2C1
            CheckInRange()
            if Check == True:
                break
            else:
                print("You have entered an invaild value, please try again.")
                time.sleep(0.2)
                continue

        while True:
            print(Player2Name + ", please enter " + Player1Name + "'s tank position at ROW from 0-7")
            GPlayer2R1 = int(input(Player2Name + "'s tank position will be at ROW: "))
            CheckDigital = GPlayer2R1
            CheckInRange()
            if Check == True:
                break
            else:
                print("You have entered an invaild value, please try again.")
                time.sleep(0.2)
                continue

        GPlayer2CR1 = str(GPlayer2C1) + str(GPlayer2R1)
        if GPlayer2CR1 in Player1List:
            Player1List.remove(GPlayer2CR1)
            print("Congratulations")
            time.sleep(1)
            print(Player2Name + " have destroyed a tank of " + Player1Name +", at column " + str(GPlayer2C1) + ", row " + str(GPlayer2R1)+ ".")
            time.sleep(1)
            print("So " + Player2Name + " can have one more in this round.")
            print(".")
            yg = yg + 1
            print(yg)
            continue
        else:
            print("Unfortunately...")
            print(Player2Name + " didn't guess it right :(")
            print(".")
            break
        
    #Check Player2 win or not
    if yg == 10:
        print("Wooooo....")
        time.sleep(1)
        print("We have the winner now.")
        time.sleep(1)
        print("It is...")
        time.sleep(1)
        print(".")
        time.sleep(0.1)
        print(".")
        time.sleep(0.2)
        print(".")
        time.sleep(0.3)
        print(".")
        time.sleep(0.1)
        print(".")
        time.sleep(0.2)
        print(".")
        time.sleep(0.2)
        print(Player2Name)
        time.sleep(2)
        print("Congratulations to " + Player2Name)
        time.sleep(0.5)
        print("You will get a TANK someday")
        time.sleep(2)
        print(Player1Name + " had got " + str(xg) + " mark(s), which is not bad.")
        time.sleep(2)
        print("See you next time...")
        break
    else:
        continue
    
    #Check Player2 win or not
    if xg == 10:
        print("Wooooo....")
        time.sleep(1)
        print("We have the winner now.")
        time.sleep(1)
        print("It is...")
        time.sleep(1)
        print(".")
        time.sleep(0.1)
        print(".")
        time.sleep(0.2)
        print(".")
        time.sleep(0.3)
        print(".")
        time.sleep(0.1)
        print(".")
        time.sleep(0.2)
        print(".")
        time.sleep(0.2)
        print(Player1Name)
        time.sleep(2)
        print("Congratulations to " + Player1Name)
        time.sleep(0.5)
        print("You will get a TANK someday")
        time.sleep(2)
        print(Player2Name + " had got " + str(yg) + " mark(s), which is not bad.")
        time.sleep(2)
        print("See you next time...")
        break
    else:
        continue
