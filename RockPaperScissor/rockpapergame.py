rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
game=[rock,paper,scissors]
user_choice=int(input('Choose 0 for rock,1 for paper and 2 scissors:'))
if user_choice>=3 or user_choice<0:
  print("You typed an invalid number..")
else:
  print(game[user_choice])
  
  comp_choice=random.randint(0,2)
  comp_choice=int(comp_choice)
  print('Computer chose:')
  print(game[comp_choice])
  
  if user_choice==0 and comp_choice==2:
    print("You Win")
  elif comp_choice==0 and user_choice==2:
    print("You Win")
  elif comp_choice==user_choice:
    print("Its a draw")
  elif comp_choice>user_choice:
    print("You Lose")  
  elif user_choice>comp_choice:
    print("You Win")