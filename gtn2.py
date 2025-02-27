import random
names=[] #list for leaderboard function
familiar=False #flag for if the player has played before
def leaderboard(): #leaderboard function
    
    f=open("ChrysScores.txt","r")
    funclist=f.read().split(",")
    for i in range(int(len(funclist)/2)): #Put names from text file into a list
        names.append([int(funclist[0]),str(funclist[1])]) 
        funclist.pop(0)
        funclist.pop(0)
    names.sort(reverse=True) #Sort list by highest score
    if len(names)==0: #If the leaderboard is empty, dont print it
        return
    print("")
    print ("-+=GRANDEST GUESSERS:=+-") #leaderboard title
    if len(names)>10: #Draw leaderboard
        for i in range(10):
            print (i+1,":",names[i][0],"  ",names[i][1])
    else:
        if len(names)==1:
            print("1:",names[0][0],"  ",names[0][1])
        else:    
            for i in range(len(names)):
                print(i+1,":",names[i][0],"  ",names[i][1])

class User: #User class stuff

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def assign_score(self, score):
        self.score = score

while True: #main loop
    print(""" 
    ╔═╡ ╥ ╥ ╔══ ╔═╡ ╔═╡
    ║ ╗ ║ ║ ╠══ ╚═╗ ╚═╗
    ╚═╝ ╚═╝ ╚══ ╞═╝ ╞═╝
    ═╦═ ╥ ╥ ╔══
     ║  ╠═║ ╠══
     ╨  ╨ ╨ ╚══
    ╔═╗ ╥ ╥ ╔╦╗ ╔═╗ ╔══ ╔═╕
    ║ ║ ║ ║ ║║║ ╠═╣ ╠══ ║ 
    ╨ ╨ ╚═╝ ╨ ╨ ╚═╝ ╚══ ╨
    With Smiley Sam! ☺
    """) #logo
    try: #Create ChrysScores file if it doesnt exist yet
       t=open("ChrysScores.txt","r")
    except:
        t=open("ChrysScores.txt","w")
    f = open("ChrysScores.txt","r") #prepare to read existing players
    input("Press Enter to start!")
    print("\n")
    print("☺ Hello! My name is Smiley Sam!") #ask player's name
    yourName=input("What's your name? ")
    user1=User(yourName, 0) #create user object
    list = f.read().split(",")
    if yourName in list: #greet depending on if a score has already been saved for this person
        print("☺ Oh! Welcome back!")
        familiar=True
    else: 
        print("☺ It's nice to meet you!")
        familiar=False
    print("")
    print("☺ Let's play Guess the Number!")
    number=random.randrange(1,100) #generate number
    guesses=0
    print("☺ I'm thinking of a number between 1 and 100. Can you guess what it is?")
    while True: #Game logic
        guesses += 1 #increase attempt count
        yourGuess=int(input("☺ What's your guess? "))
        if yourGuess==number: break #If the guess is right, stop game
        elif yourGuess>number: #otherwise provide hint
            print("☺ Nope!")
            print("☺ My number is lower!")
            print("")
        else:
            print("☺ Nope!")
            print("☺ My number is higher!")
            print("")
    print("☺ That's the one!")
    print("")
    Print("☺ You got",100-guesses+1,"points!")
    user1.assign_score(100-guesses+1) #assign player score
    decision=input("☺ Well done! Want me to save your score? (y/n)")
    if decision == "y" or decision == "Y":
        
        with open("ChrysScores.txt", "a") as f:
            if not familiar: #if the player is new, add their name and score to the text file.
                r=open("ChrysScores.txt","r")
                if len(r.read())!=0:
                    f.write(",")
                f.write(str(user1.score))
                f.write(",")
                f.write(user1.name)
            else: #If the player has played before
                f=open("ChrysScores.txt","r")
                list = f.read().split(",")
                if int(list[list.index(user1.name)-1])<user1.score: #update their score if it's higher than the previous one
                    list[list.index(user1.name)-1]=user1.score
                    g=open("ChrysScores.txt","w")
                    g.write("")
                    f=open("ChrysScores.txt","a")
                    for i in list: #convert list back to text file
                        f.write(str(i))
                        f.write(",")
    leaderboard()
    print("")
    input("☺ Thanks for playing! press enter to return to the title screen.")
