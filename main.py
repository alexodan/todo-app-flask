from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

# # home
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!!!!</p>"

# path params
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    print("tipo: ", type(post_id))
    return f'Post {post_id}'

@app.route("/")
def home():
    todo_list = [
        {'id': 1, 'title': "lavar los platos", 'complete': False},
        {'id': 2, 'title': "leer newsletter de ischargo", 'complete': False}
    ]
    return render_template("base.html", todo_list=todo_list)

@app.route("/todo/<int:todo_id>")
def get_todo_by_id(todo_id):
    todo = {'id': 1, 'title': "lavar los platos", 'complete': False}
    return render_template("todo_id.html", todo = todo)

# Verbos HTTP

# GET => obtener
# POST => crear
# PUT => sobrescribir el modelo completo
# DELETE => borrar
# PATCH => /post/:id [method=PATCH, {title: "algun titulo"}] { id, title, creation_date, ... }
# OPTIONS => ni idea
