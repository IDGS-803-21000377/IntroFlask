from flask import Flask

app = Flask(__name__)  

@app.route('/')
def index():
    return "hola mundo!!"



@app.route("/hola")
def hola():
    return"hola!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Numer:{}".format(n)


@app.route("/user/<string:user>/<int:n")
def username(user,id):
    return f"Nombre:{user} id:{id}!!!"

@app.route("/suma/<float:n1>/<float:n2")
def suma(n1,n2):
    return "la suma es {}!!!".format(n1,n2)



if __name__ == "__main__":
    app.run(debug=True)

