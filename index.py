

import random
local = ['rock','paper','scissors','admin command prompt']
local1 = ['rock','paper','scissors']
userchoice = input("choose rock paper scissors ")
computer_choice = random.choice(local1)
print("computer chose", computer_choice)
print("your choice",userchoice)

if userchoice == computer_choice:
    print("draw")
elif userchoice == "rock" and computer_choice == "paper": 
    print("paper covers rock, you lose")
elif userchoice == "paper" and computer_choice == "rock":
    print("paper covers rock, you win")
elif userchoice == "scissors" and computer_choice == "paper":
    print("scissors cut paper, you win")
elif userchoice == "paper" and computer_choice == "scissors":
    print("scissors cut paper you lose")
elif userchoice == "rock" and computer_choice == "scissors":
    print("rock breaks scissors, you win")
elif userchoice == "scissors" and computer_choice == "rock":
    print("rock breaks scissors, you lose")
elif userchoice == "admin command prompt":
    print("taskkill /f /im RPSai.exe")
    print("SUCCESS: The process RPSai.exe with PID 69420 has been terminated.")
    print("you win, cheater")
elif userchoice != local:
    print("invalid selection, stop")
else:
    print("what")