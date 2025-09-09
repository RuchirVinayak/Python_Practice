import random

scores = {"YOU": 0, "COMPUTER": 0, "TIE": 0}
rounds = int(input("How many rounds do you wanna play? 3 or 5: "))

for _ in range(rounds):
    choose = input("Choose any one among Snake(s), Gun(g), Water(w): ").lower()
    while choose not in ["s", "g", "w"]:
        choose = input("Invalid choice! Choose s, g, or w: ").lower()

    comp = random.choice(["s", "g", "w"])
    print(f"Computer chose: {comp}")

    if choose == comp:
        print("It's a tie!")
        scores["TIE"] += 1
    elif (choose == "s" and comp == "w") or (choose == "w" and comp == "g") or (choose == "g" and comp == "s"):
        print("You won this round!")
        scores["YOU"] += 1
    else:
        print("You lost this round!")
        scores["COMPUTER"] += 1

    print("Current Scoreboard:", scores)
    print("-" * 30)

# Determine final winner
if scores["YOU"] > scores["COMPUTER"]:
    print("YOU WON THE GAME!")
elif scores["YOU"] < scores["COMPUTER"]:
    print("COMPUTER WINS!")
else:
    print("THE GAME IS A TIE!")

print("Final Scoreboard:", scores)