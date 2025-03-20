from flask import Flask, render_template, request, redirect, url_for, flash, g
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from config import DevelopmentConfig
from models import db, Alumnos, Usuarios
import forms


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        # validar contraseñas
        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'error')
            return redirect(url_for('registro'))
        # ver en la base de datos si el usuario ya existe
        if Usuarios.query.filter_by(username=username).first():
            flash('El nombre de usuario ya existe', 'error')
            return redirect(url_for('registro'))

        # crear un nuevo usuario
        nuevo_usuario = Usuarios(username=username)
        nuevo_usuario.set_password(password)  # hashear la contraseña

        # enviar los datos a la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()
        # enviar mensaje de exito
        flash('Registro exitoso', 'success')
        return redirect(url_for('login'))

    return render_template("registro.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # buscar el usuario en la base de datos
        usuario = Usuarios.query.filter_by(username=username).first()

        # verificar si el usuario existe y si la contraseña es correcta
        if usuario and usuario.check_password(password):
            user = User(usuario.id)
            login_user(user)
            return redirect(url_for('index'))
        else:
            # enviar mensaje de error
            flash('Usuario o contraseña incorrectos', 'error')
    return render_template("login.html")

#cerrar sesion
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/protegida")
@login_required
def protegida():
    return "Esta es una ruta protegida. Solo usuarios autenticados pueden ver esto."


@app.route("/")
@app.route("/index")
@login_required
def index():
    create_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()  # Select from alumnos
    return render_template("index.html", form=create_form, alumno=alumno)

@app.route("/detalles", methods=['GET', 'POST'])
@login_required
def add():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        nom = alum1.nombre
        ape = alum1.apaterno
        email = alum1.email
    return render_template("detalles.html", form=create_form, nom=nom, ape=ape, email=email)

@app.route("/Alumnos1", methods=['GET', 'POST'])
@login_required
def Alumnos1():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre=create_form.nombre.data, apaterno=create_form.apaterno.data, email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("Alumnos1.html", form=create_form)

@app.route('/modificar', methods=['GET', 'POST'])
@login_required
def modificar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = str.rstrip(alum1.nombre)
        create_form.apaterno.data = alum1.apaterno
        create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum1.id = id
        alum1.nombre = str.rstrip(create_form.nombre.data)
        alum1.apaterno = create_form.apaterno.data
        alum1.email = create_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("modificar.html", form=create_form)

@app.route('/eliminar', methods=['GET', 'POST'])
@login_required
def eliminar():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("eliminar.html", form=create_form)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()