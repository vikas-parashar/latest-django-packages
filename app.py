from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mandrill import Mandrill
from getenv import env
from scr import *


import dotenv
dotenv.read_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///latest-package'
db = SQLAlchemy(app)

app.config['MANDRILL_API_KEY'] = env('API_KEY')
mandrill = Mandrill(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

# Set "homepage" to index.html
@app.route('/')
def index():
    # package_finder()
    # new_package_list = difference()

    # list_finder()
    # new_to_old()


    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            print reg.email
            mcl = call_other_functions()
            print mcl
            mandrill.send_email(
                from_email=env('FROM_MAIL'),
                to=[{'email': 'svnitvikas@gmail.com'}],
                # text="hello world"
                html=render_template("mail.html", mcl=mcl)
            )

            return render_template('success.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()