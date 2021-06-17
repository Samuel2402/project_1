from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SQLALchemy_DATABASE_URI'] = "sqlite:///"
app.config['SECRET_KEY'] = "TEST"

db = SQLAlchemy(app)

class Register(db.Model):
    name = db.Column(db.String(30), nullable=False, primary_key=True)

class RegisterForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

db.create_all()

@app.route('/', methods=["GET","POST"])
def home():
    form = RegisterForm()
    if form.validate_on_submit():
        person = Register(name=form.name.data)
        db.session.add(person)
        db.session.commit()
    registrees = Register.query.all()
    return render_template("home.html", registrees=registrees, form=form)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

########################################### old ############################

#from flask import Flask, render_template
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField # We will only use StringField and SubmitField in our simple form.
#from wtforms.validators import DataRequired, Length, ValidationError

#app = Flask(__name__)

#app.config['SQLALchemy_DATABASE_URI'] = "sqlite:///"
#app.config['SECRET_KEY']='fdghjskayuedbnakcxgahqwoqpqn' #Configure a secret key for CSRF protection.

########################################### flask set-up  #######################################################

#class UserCheck:
#    def __init__(self, banned, message=None):# Here we set up the class to have the banned and message attributes. banned must be passed through at declaration.
#        self.banned = banned
#        if not message:
#            message = 'Please choose another username' # If no message chosen, then this default message is returned.
#        self.message = message
#
#    def __call__(self, form, field):
         # Here we define the method that is ran when the class is called. If the data in our field is in the list of words then raise a ValidationError object with a message.
#        if field.data.lower() in (word.lower() for word in self.banned):
#            raise ValidationError(self.message)

#class myForm(FlaskForm):
#    username = StringField('Username', validators=[
#        DataRequired(),
#        # We call our custom validator here, and pass through a message to override the default one. We pass through the list of banned usernames as a list.
#        UserCheck(message="custom rejection message",banned = ['root','admin','sys']),
#        Length(min=2,max=15)
#        ])
#    submit = SubmitField('Sign up')

################################### app routes ###############################################################

#@app.route('/', methods=['GET','POST'])
#def postName():
#    form = myForm()
#    if form.validate_on_submit():
#        username = form.username.data
#        return render_template('home.html', form = form, username=username)
#    else:
#        return render_template('home.html', form = form, username="")

########################### end ##################################################

#if __name__ == '__main__':
#    app.run(debug=True)