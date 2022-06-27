import os
#from MainScores
from Utils import SCORES_FILE_NAME
def add_score(difficulty):

    POINTS_OF_WINNING = (difficulty*3)+5

    if os.path.exists("/tmp/Scores.txt"):
        fread = open("/tmp/Scores.txt", "r+")
        current_score = fread.read()
        new_score = int(current_score) + POINTS_OF_WINNING
        fwrite = open("/tmp/Scores.txt",'w+')
        fwrite.write(str(new_score))
        fwrite.close()
    else:
        fwrite = open("/tmp/Scores.txt", "w+")
        fwrite.write(str('0'))
        fwrite.close()

