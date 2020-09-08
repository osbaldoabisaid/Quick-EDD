#intento de conexion a EDD _HA
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL

app = Flask(__name__)
#CONEXION CON MYSQL
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "osba1234"
app.config["MYSQL_DB"] = "test"
mysql = MySQL(app)

#CONFIGURACIONES  
app.secret_key = "mysecretkey"

@app.route("/")
def EDD():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM quick_edd")
    data = cur.fetchall()
    return render_template("EDD.html", quick_edd = data) 
    
    #AGREGAR CONTACTO 

@app.route("/add_contact", methods=["POST"])
def add_contacts():
    if request.method == "POST":
       Cliente = request.form["Cliente"]
       Módelo = request.form["Módelo"]
       Procesador = request.form["Procesador"]
       Grupo = request.form["Grupo"]
       Serie  = request.form["Serie"]
       Partición = request.form["Partición"]
       Producto = request.form["Producto"]
       cur = mysql.connection.cursor()
       cur.execute("INSERT INTO quick_edd (Cliente, Módelo, Procesador, Grupo, Serie , Partición, Producto) VALUES (%s, %s, %s, %s, %s, %s, %s)",
       (Cliente, Módelo, Procesador, Grupo, Serie , Partición, Producto))
       mysql.connection.commit()
       flash("Contacto Agregado Correctamente!")
       return redirect(url_for("EDD"))

    #EDITAR CONTACTO 

@app.route("/edit/<id>", methods = ["POST", "GET"])
def get_quick_edd(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM quick_edd WHERE id = %s", [id])
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template("edit-EDD.html", quick_edd = data[0])

    #ACTUALIZAR CONTACTO 

@app.route("/update/<id>", methods = ["POST"])
def update_quick_edd(id):
    if request.method == "POST":
        Cliente = request.form["Cliente"]
        Módelo = request.form["Módelo"]
        Procesador = request.form["Procesador"]
        Grupo = request.form["Grupo"]
        Serie  = request.form["Serie"]
        Partición = request.form["Partición"]
        Producto = request.form["Producto"]
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE quick_edd
            SET Cliente = %s,
                Módelo = %s, 
                Procesador = %s,
                Grupo = %s,
                Serie  = %s,
                Partición = %s,
                Producto = %s
            WHERE id = %s
         """, (Cliente, Módelo, Procesador, Grupo, Serie, Partición, Producto, id))
        flash("Contacto Actualizado Correctamente!")
        mysql.connection.commit()
        return redirect(url_for("EDD"))
   
    #VORRAR CONTACTO

@app.route("/delete/<string:id>")
def delete_quick_edd(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM quick_edd   WHERE id = {0}" .format(id))
    mysql.connection.commit()
    flash("Contacto Borrado")
    return redirect(url_for("EDD"))

if __name__ == "__main__":
    app.run(port = 3000, debug = True)