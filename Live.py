# This is a sample Python script.
import os
import shutil
columns = shutil.get_terminal_size().columns
def welcome(name):
 #os.system('cls')
 try:
     NameUserInput = str(input('enter your name\n'.center((columns))))
 except EOFError:
   pass
 print(f"Hello \033[1m{NameUserInput}\033[0m and welcome to the World of Games (WoG).Here you can find many cool games to play".center(columns))

def load_game():
   print(f'Please choose a game to play:'.center((columns)))
   print(f'1. Memory Game - a sequence of numbers will appear for a short time and you have to guess it back'.center((columns)))
   print(f'2. Guess Game - guess a number and see if you chose like the computer'.center((columns)))
   print(f'3. Currency Roulette - try and guess the value of a random amount of USD in ILS'.center((columns)))
   while True:
    try:
       GameUserInput = int(input("enter game number "))
    except ValueError:
       print("invalid input. please enter digit between 1 to 3 ")
       continue
    print("Game number:", GameUserInput)
    if (1<= GameUserInput <= 3):
      break
    else:
        print("not a valid selction,please try again  ")
        continue
   print('GameUserInput')

   print(f'Please choose a game level . 1- easy to 5-hard :')
   while True:
    try:
       GameUserLevelInput = int(input(" GameUserLevelInput "))
       print("Game level number:", GameUserLevelInput)
    except ValueError:
       print("invalid input. please enter digit between 1 to 5 ")
       continue
    if (1<=GameUserLevelInput <= 5):
         break
    else:
         print("not a valid selction,please try again  ")
         #GameUserLevelInput = int(input("enter game level "))
         continue

   return[GameUserLevelInput,GameUserInput]

