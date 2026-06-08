from flask import Flask, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

conexion = sqlite3.connect("dev.db", 
check_same_thread=False)

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")
conexion.commit()


@app.route("/registro", methods=["GET", "POST"])
def registro():
    
    
    if request.method == "POST":
        
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        senha_hash = generate_password_hash(senha)
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha_hash)
        )
        conexion.commit()
        return redirect(url_for("login"))

    return render_template("registro.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()

        if usuario:
            senha_hash = usuario[3]
            if check_password_hash(senha_hash, senha):
                return "Senha correta!"
            else:
                return "Senha incorreta."
        else:
            return "Usuário não encontrado."

    return render_template("login.html")


@app.route("/")
def index():
    return render_template("registro.html")


if __name__ == "__main__":
    app.run(debug=True)
    






 




