import random
names=[] #list for leaderboard function
familiar=False #flag for if the player has played before
def leaderboard(): #leaderboard function
    names=[] #reset names list
    f=open("ChrysScores.txt","r")
    funclist=f.read().split(",")
    for i in range(int(len(funclist)/2)): #Put names from text file into a list
        names.append([int(funclist[0]),str(funclist[1])]) 
        funclist.pop(0)
        funclist.pop(0)
    names.sort(reverse=True) #Sort list by highest score
    if len(names)==0: #If the leaderboard is empty, dont print it
        print("if there were any names in the leaderboard, it would be here")
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
    while True:
        pressStart=input("S to start, LB for leaderboard, X to exit ")
        if pressStart=="LB": leaderboard()
        elif pressStart=="X": quit()
        elif pressStart=="S": break
        else: print("ERROR. Please choose from the list of inputs given.")

    print("\n")
    print("☺ Hello! My name is Smiley Sam!") #ask player's name
    yourName=input("What's your name? ")
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
    print("☺ I'm thinking of a whole number between 1 and 100. Can you guess what it is?")
    while True: #Game logic
        guesses += 1 #increase attempt count
        try:
            yourGuess=int(input("☺ What's your guess? "))
        except ValueError:
            print("☺ That's not a whole number, silly!")
            print("☺ Try again.")
            print("")
            guesses -= 1
            continue
        
        if yourGuess==number: break #If the guess is right, stop game
        elif yourGuess>number: #otherwise provide hint
            print("☺ Nope!")
            print("☺ My number is lower!")
            print("")
        else:
            print("☺ Nope!")
            print("☺ My number is higher!")
            print("")
    print("☺ That's the one!") #when game is won
    print("")
    print("☺ You got",100-guesses+1,"points!")
    decision=input("☺ Well done! Want me to save your score? (y/n)")
    if decision == "y" or decision == "Y":
        
        with open("ChrysScores.txt", "a") as f:
            if not familiar: #if the player is new, add their name and score to the text file.
                r=open("ChrysScores.txt","r")
                if len(r.read())!=0:
                    f.write(",")
                f.write(str(100-guesses+1))
                f.write(",")
                f.write(yourName)
            else: #If the player has played before
                f=open("ChrysScores.txt","r")
                list = f.read().split(",")
                if int(list[list.index(yourName)-1])<100-guesses+1: #update their score if it's higher than the previous one
                    list[list.index(yourName)-1]=100-guesses+1
                    g=open("ChrysScores.txt","w")
                    f=open("ChrysScores.txt","a")
                    for i in list: #convert list back to text file
                        f.write(str(i))
                        f.write(",")
    leaderboard()
    print("")
    input("☺ Thanks for playing! press enter to return to the title screen.")