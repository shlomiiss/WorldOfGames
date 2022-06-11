

#def score_server()
from Utils import BAD_RETURN_CODE
from flask import Flask ,render_template
#C:/Users/SIssler/PycharmProjects/WorldOfGames/templates')
app = Flask(__name__,template_folder='templates')

# # using default
@app.route('/')
def index ():
    try:
       f = open("Scores.txt", 'r')
    except OSError:
        return render_template('error.html', ERROR=BAD_RETURN_CODE)
    with f:
     Last_scores = f.read()
     print(Last_scores)
    return render_template('index.html', SCORE=Last_scores)




app.run(host='127.0.0.1', debug=True, port=30000)

#if __name__ == "__main__":
#   app.run()

