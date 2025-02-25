import random
familiar=False
def leaderboard(): #leaderboard function
    names=[]
    f=open("ChrysScores.txt","r")
    funclist=f.read().split(",")
    for i in range(int(len(funclist)/2)):
        names.append([int(funclist[0]),str(funclist[1])])
        funclist.pop(0)
        funclist.pop(0)
    names.sort(reverse=True)
    print (names)

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
f = open("ChrysScores.txt","r") #prepare to read existing players
input("Press Enter to start!")
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
number=random.randrange(1,100)
guesses=0
print("☺ I'm thinking of a number between 1 and 100. Can you guess what it is?")
while True:
    guesses += 1 #increase attempt count
    yourGuess=int(input("☺ What's your guess? "))
    if yourGuess==number: break #If the guess is right, stop game
    elif yourGuess>number: #otherwise provide hint
        print("☺ Nope!","\n","☺ My number is lower than that!")
        print("")
    else:
        print("☺ Nope!","\n","☺ My number is higher than that!")
        print("")
print("☺ That's the one!")
print("")
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
                g=open("ChrysScore.txt","w")
                g.write("")
                f=open("ChrysScores.txt","a")
                for i in list: #convert list back to text file
                    f.write(i)
                    f.write(",")
leaderboard()