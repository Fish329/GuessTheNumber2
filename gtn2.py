import random
print("""
╔═╡ ╥ ╥ ╔══ ╔═╡ ╔═╡
║ ╗ ║ ║ ╠══ ╚═╗ ╚═╗
╚═╝ ╚═╝ ╚══ ╞═╝ ╞═╝
═╦═ ╥ ╥ ╔══
 ║  ╠═║ ╠══
 ╨  ╨ ╨ ╚══
╔═╗ ╥ ╥ ╔╦╗ ╔═╗ ╔══ ╔═╗
║ ║ ║ ║ ║║║ ╠═╣ ╠══ ║
╨ ╨ ╚═╝ ╨ ╨ ╚═╝ ╚══ ╨
With Smiley Sam! ☺
""")
f = open("Scores.txt","r")
input("Press Enter to start!")
print("\n")
print("☺ Hello! My name is Smiley Sam!")
yourName=input("What's your name? ")
print("")
list = f.read().split(",")
if yourName in list:
    print("☺ Oh! Welcome back!")
else: 
    print("☺ It's nice to meet you!")
print("☺ Let's play Guess the Number!")
number=random.randrange(1,100)
guesses=0
print("")
print("☺ I'm thinking of a number between 1 and 100. Can you guess what it is?")
while True:
    guesses += 1
    yourGuess=input("☺ What's your guess? ")
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