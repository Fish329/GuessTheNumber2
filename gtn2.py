import random
def leaderboard():
    names=[]
    f=open("ChrysScores.txt","r")
    funclist=f.read().split(",")
    print(funclist)
    print(len(funclist
    ))
    for i in range(int(len(funclist)/2)):
        names.append([int((funclist[0])),str(funclist[1])])
        funclist.pop(0)
        funclist.pop(1)
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
""")
f = open("ChrysScores.txt","r")
input("Press Enter to start!")
print("\n")
print("☺ Hello! My name is Smiley Sam!")
yourName=input("What's your name? ")
print("")
list = f.read().split(",")
if yourName in list:
    print("☺ Oh! Welcome back!")
    familiar=False
else: 
    print("☺ It's nice to meet you!")
    familiar=True
print("☺ Let's play Guess the Number!")
number=5 #random.randrange(1,100)
guesses=0
print("")
print("☺ I'm thinking of a number between 1 and 100. Can you guess what it is?")
while True:
    guesses += 1
    print(guesses)
    yourGuess=int(input("☺ What's your guess? "))
    if yourGuess==number: break
    elif yourGuess>number: 
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
        if not familiar:
            r=open("ChrysScores.txt","r")
            if len(r.read())!=0:
                f.write(",")
            f.write(str(100-guesses+1))
            f.write(",")
            f.write(yourName)
        else:
            pass #TODO: find out how to locate player's name, then replace the score (which should be right before it in the list)
leaderboard()