
from Live import welcome,load_game
from random import randrange, random
def play(Game, Difficulty):
 while(True):
  if (Game == 2): # 2 is GuessGame
     print(f'*** You are in Memory Guess Game *** in level {Difficulty}')
     SecretNumber = generate_number(Difficulty)
     UserChooseInput = get_guess_from_user()
     compare_results(SecretNumber,UserChooseInput)
  else:
    print('wrong1233')
def generate_number(Difficulty):
  SecretNumber = randrange(1,5*Difficulty,1)
  print(f'The number is {SecretNumber}')
  return (SecretNumber)

def get_guess_from_user():
  while (True):
   UserChooseInput = input(f'Please choose  number between 1 to 20  ')
   print(f'The choosen number is {UserChooseInput}')
   if (UserChooseInput.isdigit()):
     return (UserChooseInput)
   else:
    print("valid input are digits only. try again")


def compare_results(SecretNumber, UserChooseInput):
     if int(SecretNumber) == int(UserChooseInput):
        print("Nice")
        return(True)
     else:
        print("try again")
        return (False)


