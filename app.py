from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:02November19961!@34.105.237.106:3306/newdb"    # 'sqlite:///data.db' 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

############################# INTRO - making a working website ###########################################################

#from flask import Flask

#app = Flask(__name__)

#@app.route('/')
#@app.route('/home')
#def hpme(): 
#    return "Home page"

# @app.route('/about')
# def about_page():
#    return "About page" 

#@app.route('/squared/<num>')
#def squared(num):
#    number = int(num)
#    result = number*number
#    return str(result)

#if __name__=='__main__':
#    app.run(debug=True)

# indpent lines of code, i have hashed out the first and last 2 lines (as they are repeats)

#################################### old - Cities, Countries ########################################

#class Countries(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(30), nullable=False)
#    cities = db.relationship('Cities', backref='country') 

#class Cities(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(30), nullable=False)
#    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

################################## old - Users ##########################################

#class Users(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    first_name = db.Column(db.String(30), nullable=False)
#    last_name = db.Column(db.String(30), nullable=False)


if __name__ == "__main__":
    app.run(debug=True)