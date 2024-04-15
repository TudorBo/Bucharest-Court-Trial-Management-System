from flask import Flask, render_template
from flask_mysqldb import MySQL

# add blueprints
from dosare import dosare
from legi import legi
from judecatori import judecatori
from directii import directii
from participanti import participanti
from tipuri_participanti import tipuri_participanti

app = Flask(__name__)
app.secret_key = "secret key"

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'tribunal'

mysql = MySQL(app)

# register blueprints
app.register_blueprint(legi)
legi.mysql = mysql

app.register_blueprint(dosare)
dosare.mysql = mysql

app.register_blueprint(judecatori)
judecatori.mysql = mysql

app.register_blueprint(directii)
directii.mysql = mysql

app.register_blueprint(participanti)
participanti.mysql = mysql

app.register_blueprint(tipuri_participanti)
tipuri_participanti.mysql = mysql


@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()