
 # 11. Create a Flask application which listens to
# # port 30000 and has 2 routes:
# # from random import randint
from flask import Flask

app = Flask(_name_)
app.run(host='127.0.0.1', debug=True, port=30000)
#
#
# # using default
# @app.route('/content')
# def print_content(user_name = 'no one'):
#     my_file = open("words.txt", "r")
#     for line in my_file:
#         print(line, end='')
#     return line, 200 # status code
#
# @app.route('/register')
# def print_content_new(user_name = 'no one'):
#     new_file = open("Words1.txt","w")
#     new_file.write("Hello")
#     new_file.close()
#     return "success", 201 # status code
# # accessed via <HOST>:<PORT>/welcome
#
#
# # host is pointing at local machine address
# # debug is used for more detailed logs + hot swaping
# # the desired port - feel free to change
# #  /content - which returns the content of
# # any txt file and status code 200
# # (e.g: localhost:4000/content).
# #  /register - which writes the word “hello”
# # into any txt file and return “success” and
# # status code 201 as a response
# # (e.g: localhost:4000/register).
#
#
#
# # Challenge:
# #12. Create an image from code (png file) Hint:
# # # use Pillow
# I need explanation what is needed at this challenge