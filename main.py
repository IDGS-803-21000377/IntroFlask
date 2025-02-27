from flask import Flask, render_template,request
import forms 

app = Flask(__name__)  

@app.route('/')
def index():
    lista = ["Juan","Pedro","Maria"]
    grupo = "IDGS803"

    return render_template("index.html",grupo=grupo,lista = lista)

@app.route("/Alumnos", methods=["POST","GET"])
def alumnos():
    mat= ''
    nom=''
    edad=''
    correo=''
    ape = ''
    alumno_clase= forms.UserForm(request.form)
    if(request.method) == 'POST':
     mat = alumno_clase.matricula.data
     nom = alumno_clase.nombre.data
     ape = alumno_clase.apellidos.data
     edad = alumno_clase.edad.data
     correo = alumno_clase.correo.data
    
    return render_template("Alumnos.html",form =alumno_clase,mat=mat, nom= nom,ape= ape, edad= edad, correo= correo)


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
    precio_boleto = 12.00
    descuento = 0
    mensaje = ""

    if request.method == "POST":
        name = request.form.get("nombre", "").strip()
        cant_boletos = request.form.get("cantidad", "0").strip()
        tiene_cineco = request.form.get("cineco") == "Sí"

        if not name:
            mensaje = "Por favor, ingresa tu nombre."
        elif not cant_boletos.isdigit():
            mensaje = "Por favor, ingresa un número válido de boletos."
        else:
            cant_boletos = int(cant_boletos)

            if cant_boletos > 7:
                mensaje = "El límite de compra es de 7 boletos."
            else:
                total_sin_descuento = cant_boletos * precio_boleto

                if 2 < cant_boletos < 5:
                    descuento = 0.10  
                elif cant_boletos >= 5:
                    descuento = 0.15  

                if tiene_cineco:
                    descuento += 0.10  

                total_pagar = total_sin_descuento * (1 - descuento)

                mensaje = (
                    f"Tu nombre es {name}. Compraste {cant_boletos} boletos. "
                    f"Precio total: ${total_sin_descuento:.2f}. "
                    f"Descuento aplicado: {descuento*100}%. "
                    f"Total a pagar: ${total_pagar:.2f}."
                )

    return render_template("taquilla.html", result=mensaje)




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
