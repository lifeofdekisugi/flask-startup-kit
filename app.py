from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import  wraps


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DATABASE.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'My secret key' #please change this
app.config['JSON_SORT_KEYS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({
                'response' : 'Token is missing !!',
                'message' : 'If you are having any problem tweet me @lifeofdekisugi'
                }), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id = data['public_id']).first()
        except:
            return jsonify({'response' : 'Token is invalid !!'}), 401
        # returns the current logged in users contex to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated

@app.route('/')
def hello_world():
    return ({
        'response' : 'working !!',
        'author' : 'Shahir Islam',
        'repo-link' : 'https://github.com/lifeofdekisugi/flask-startup-kit',
        'more-links' : '/sign-up , /login, /home (you need to use JWT token)'
        })
    
@app.route('/sign-up', methods=['POST'])
def sign_up():
    try:
        signUpData = request.form
                
        name = signUpData['name']
        email = signUpData['email']
        hashed_password = generate_password_hash(signUpData['password'] , method='sha256')
        
        new_user = User(public_id=str(uuid.uuid4()),name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            'response ' : 'success',
            'next-step' : '/login'
            })
    except Exception:
        return jsonify({
            'response ' : 'error',
            'next-step' : 'Please Try Again'
            }) 

@app.route('/login', methods=['POST'])
def login():
    
    auth = request.form
    
    email = auth['email']
    password = auth['password']
    
    if not auth or not email or not password:
        #return make_response('Could not Verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
        return jsonify({'response' : 'Login Failed'})
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        #return make_response('Could not Verify', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
        return jsonify({'response' : 'Email not found :('})
    
    if check_password_hash(user.password, password):
        token = jwt.encode({'public_id' : user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])
        
        return jsonify({
            'response' : 'success',
            'token' : token.decode('UTF-8'),
            }) 

@app.route('/home')
@token_required
def app_home(current_user):
    
    if not current_user:
        return jsonify({
            'response' : 'error',
            'message' : 'You are not authenticated. \n Please Login and try again.'
            })
    
    return jsonify({
        'response' : 'success',
        'message' : 'You did it mate.'
    })

if __name__ == "__main__":
    app.run(debug=True) #before deploy change debug to False