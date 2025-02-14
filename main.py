from flask import Flask, render_template,request

app = Flask(__name__)  

@app.route('/')
def index():
    lista = ["Juan","Pedro","Maria"]
    grupo = "IDGS803"

    return render_template("index.html",grupo=grupo,lista = lista)

@app.route("/OperasBas", methods=["GET", "POST"])
def operas():
    res = 0
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        res = "La suma de {} y {} es {}".format(num1, num2, int(num1) + int(num2))
    return render_template("OperasBase.html", res=res)

@app.route("/resultado",methods=["GET","POST"])

def resultado():
    
    

    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La suma de este {} y {} es {}".format(num1,num2,int(num1)+int(num2))
    return render_template("OperasBase.html")




@app.route("/boletos", methods=["GET", "POST"])
def boletos():
    result = 0

  

        
    return render_template("taquilla.html", result = result)
     




@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")
@app.route("/ejemplo2")

def funcion1():
    return render_template

def ejemplo2():
    return render_template("ejemplo2.html")




@app.route("/hola")
def hola():
    return "Hola!!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Número: {}".format(n)

@app.route("/user/<string:user>/<int:id>")
def username(user, id):
    return f"Nombre: {user} id: {id}!!!"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es {}!!!".format(n1 + n2)

@app.route("/form1")
def form1():
    return '''
        <form>
        <label>Nombre:</label>
        <input type ="text" name = "nombre placeholder= "nombre">
        </br>
        <label>Nombre:</label>
        <input type ="text" name = "nombre placeholder= "nombre">
        </br>
        <label>Nombre:</label>
        <input type ="text" name = "nombre placeholder= "nombre">
        </br> 


    '''


if __name__ == "__main__":
    app.run(debug=True)
