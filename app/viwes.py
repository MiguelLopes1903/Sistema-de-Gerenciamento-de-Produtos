from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/inicio")
def homepage():
    return render_template("inicio.html")

@app.route("/Financeiro")
def financeiro():
    return render_template("financeiro.html")

@app.route("/Produtos", methods=["GET", "POST"])
def produtos():
    if request.method == "POST":
        arquivo = request.files.get("foto_produto")
        if arquivo and allowed_file(arquivo.filename):
            filename = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('produtos'))
    return render_template("produtos.html")

@app.route("/Pedidos")
def pedidos():
    return render_template("pedidos.html")

if __name__ == "__main__":
    app.run(debug=True)
