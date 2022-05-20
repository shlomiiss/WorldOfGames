import GuessGame
import MemoryGame
import CurrencyRouletteGame
from Live import welcome,load_game

name = ''
welcome(name)
while True:
 GameUserLevelInput,GameUserInput = load_game()
 print(f'"you selected game \033[1m{GameUserInput}\033[0m in level \033[1m{GameUserLevelInput}\033[0m. The game will run soon and good luck')
 if GameUserInput == 1:
    MemoryGame.play(GameUserInput,GameUserLevelInput)
 elif GameUserInput == 2:
    GuessGame.play(GameUserInput,GameUserLevelInput)
 elif GameUserInput == 3:
    CurrencyRouletteGame.play(GameUserInput,GameUserLevelInput)
 elif GameUserInput == 'Q':
    break

result = (GameUserInput,GameUserLevelInput)
print(result)