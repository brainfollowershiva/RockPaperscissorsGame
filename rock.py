import random
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
a=[rock,paper,scissors]
s=int(input("What do you want , Type 0 for Rock ,1 for Paper,2 for scissors "))
if s==0:
    print(a[0])
    b=random.randint(1,2)
    c=a[b]
    if c==a[1]:
        print("The Computer chose ",a[b])
        print("You Won")
    else:
        print("The Computer chose ",a[b])
        print("You Lose")

elif s==1:
    print(a[1])
    d= random.randint(0, 2)
    e=a[d]
    if e==a[2]:
      print("The Computer chose ", a[2])
      print("You Won")
    elif e==a[0]:
      print("The Computer chose ", a[0])
      print("You Lose")
    else:
     print("Invalid try again ")

elif s==2:
    print(a[2])
    f=random.randint(0,1)
    g=a[f]
    if g==a[1]:
      print("The Computer chose ", a[1])
      print("You Lose")
    elif g==a[0]:
      print("The Computer chose ", a[0])
      print("You Won")
    else:
      print("Invalid try again")
else:
    print("You typed an invalid number, you lose!")