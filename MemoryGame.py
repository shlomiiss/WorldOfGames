
from Live import welcome,load_game
from random import randrange
import os
from time import sleep
MaxRandom = 101
RandomList=[]


def play(Game, Difficulty):
 while True:
  if (Game == 1): # 1 is Memory Game
     print(f'*** You are in Memory Game Game *** in level {Difficulty}')
     RandomList = generate_sequence(Difficulty)
     UserChooseList = get_list_from_user(Difficulty)
     is_list_equal(RandomList,UserChooseList)
  else:
    print('wrong')
def generate_sequence(Difficulty):
  RandomList = [None]*Difficulty*2
  for i in range(0,len(RandomList)):
    RandomList[i] = randrange(1,MaxRandom,1)
  print(f'The memory list to remember is {RandomList}\n')
  for c in range(2*Difficulty, 0, -1):
      print(f'Time left is:{c}',end='\r')
      sleep(1)
  cls = os.system('cls')
  return (RandomList)

def get_list_from_user(Difficulty):
 UserChooseList= []
 while (True):
  UserChooseList = input(f'Please enter {2*Difficulty}  numbers between 1 to 101  \n').split()
  for item in UserChooseList:
      try:
          int_value = int(item)
          print(int_value)
      except ValueError or TypeError:
       print("not digits were entered. pls enter digits only")
       break
  else:
        print(f'The  numbers are {UserChooseList}')
        return (UserChooseList)

def is_list_equal(RandomList, UserChooseList):
     UserList = set(map(int,UserChooseList))
     RanList = set(RandomList)
     print(RandomList)
     print(UserChooseList)
     if (RanList==UserList):
        print("match")
        return(True)
     else:
        print("try again")
        return (False)


