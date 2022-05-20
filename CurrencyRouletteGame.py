from Live import welcome,load_game
from random import randrange, random
from currency_converter import CurrencyConverter

def play(Game, Difficulty):
 while(True):
  if (Game == 3): # 3 is Roulette Game
     print(f'*** You are in Currency Roulette Game Game *** in level {Difficulty}\n')
     RandomNumber,GuessIntervalDown,GuessIntervalUp = get_money_interval(Difficulty)
     get_guess_from_user(RandomNumber,GuessIntervalDown,GuessIntervalUp)

     #get_guess_from_user()


def get_money_interval(Difficulty):
    c = CurrencyConverter()
    RandomNumber = randrange(5,100,1)
    MoneyValue = c.convert(RandomNumber,'USD','ILS')
    GuessIntervalDown = MoneyValue - (5 - Difficulty)
    GuessIntervalUp = MoneyValue + (5 + Difficulty)
    print(RandomNumber,int(GuessIntervalDown),int(GuessIntervalUp))
    return (RandomNumber,int(GuessIntervalDown),int(GuessIntervalUp))

def get_guess_from_user(RandomNumber,GuessIntervalDown,GuessIntervalUp):
    while(True):
     UserGuessInput = (input(f'For {RandomNumber} in USD ,Please enter your guess how much is it in ILS  \n'))
     if not (UserGuessInput.isdigit()):
        print("valid input are digits only. try again")
        continue
     elif (GuessIntervalDown <= int(UserGuessInput)<=GuessIntervalUp):
        print("Well Done")
        return (True)
     else:
        print("Wrong guess")
        return (False)

