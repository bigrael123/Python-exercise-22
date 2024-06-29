import random as r

jokenpo = ["Stone", "Scissor", "Paper"]
scoreboard = ["","",""]
games = 0
victory = 0
draw = 0
print(f"To play jokenpo select an item: 1 - {jokenpo[0]}, 2 - {jokenpo[1]} 3 - {jokenpo[2]}")
while(True):
    while(True):
        try:
            selected = int(input("type the number of your item: "))
            if(selected <= 0 or selected >= 4):
             print("Please, type a number between 1 and 3")
            else:
                break
        except ValueError:
            print("Please, type a number.")
        
    print(f"You selected: {jokenpo[selected-1]}")
    selected_cpu = r.randrange(1,4)
    print(f"The cpu selected {jokenpo[selected_cpu-1]}")
    if((selected == 1 and selected_cpu == 2) or (selected == 2 and selected_cpu == 3) or (selected == 3 and selected_cpu == 1)):
        scoreboard[games] = "You won"
        print(scoreboard[games])
        victory+=1
    elif((selected_cpu == 1 and selected == 2) or (selected_cpu == 2 and selected == 3) or (selected_cpu == 3 and selected == 1)):
          scoreboard[games] = "You lost"
          print(scoreboard[games])
    else:
         draw+=1
         scoreboard[games] = "Draw"
         print(scoreboard[games] )
    games += 1
    if(games == 3):
        print("The game ended and here is the history:")
        for score in scoreboard:
             print(score)
        games = 0
        if(victory == 2 or (draw == 2 and victory == 1)):
             print("You won the best of 3")
        elif(draw == 3):
             print("The game ended in a draw")
        else:
             print("The cpu won")
        break