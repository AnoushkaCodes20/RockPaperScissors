import random
play=["Rock","Paper","Scissors"]
choice=int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors  "))
print("You chose ",play[choice])
if play[choice]=="Rock":
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
)
elif play[choice]=="Paper":
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
computer_choice=random.randint(0,2)
if computer_choice==0:
    print("Computer chose: Rock"'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif computer_choice==1:
    print("Computer chose: Paper"'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
    print("Computer chose: Scissors"'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
#rock=0 paper=1 scissors=2
if choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice > choice:
    print("You lose")
elif choice==2 and computer_choice==0:
    print("You lose")
elif choice==1 and computer_choice==0:
    print("You win")
elif choice==2 and computer_choice==1:
    print("You win")
elif computer_choice == choice:
    print("It's a draw")
else:
    print("You entered an invalid value.")











