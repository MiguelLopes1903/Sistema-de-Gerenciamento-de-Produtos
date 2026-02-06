from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# --- 1. CONFIGURAÇÃO DO BANCO DE DADOS (SQLite) ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projeto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- 2. MODELO DE DADOS ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantidade = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'quantidade': self.quantidade
        }

# --- 3. CRIAÇÃO DAS TABELAS ---
with app.app_context():
    db.create_all()

# ================================================================
#               ROTAS DE NAVEGAÇÃO WEB (CRUD VISUAL)
# ================================================================

# ROTA 1: Exibir Lista e Formulário de Criação (READ)
@app.route("/")
def index():
    all_users = User.query.all()
    return render_template("adicao.html", users=all_users)

# ROTA 2: Processar Criação (CREATE)
@app.route('/create', methods=['POST'])
def create_user_page():
    name = request.form.get('name')
    quantidade = request.form.get('quantidade')
    
    if name and quantidade:
        new_user = User(name=name, quantidade=quantidade)
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            pass
    
    return redirect(url_for('index'))

# ROTA 3: Exibir Formulário de Edição
@app.route('/edit/<int:user_id>')
def edit_user_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

# ROTA 4: Processar Modificação (UPDATE)
@app.route('/update/<int:user_id>', methods=['POST'])
def update_user_page(user_id):
    user = User.query.get_or_404(user_id)
    user.name = request.form.get('name')
    user.quantidade = request.form.get('quantidade')
    db.session.commit()
    return redirect(url_for('index'))

# ROTA 5: Processar Exclusão (DELETE)
@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user_page(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True, port=8000)
