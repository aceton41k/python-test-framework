import bcrypt
import jwt
from flask import Flask, jsonify, request, flash, redirect, url_for, render_template
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pydb_user:pydb123@localhost/pydb'
app.config['SECRET_KEY'] = 'abracadabra'
db = SQLAlchemy(app)


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    job_id = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'job_id': self.job_id
        }


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        user = Users.query.filter_by(login=login).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


@app.route('/register', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'login' not in data or 'password' not in data:
        return jsonify({'error': 'login and password are required.'}), 400

    login1 = data['login']
    password = data['password']

    try:
        user = Users(login1=login1, password=password)
        db.session.add(user)
        db.session.commit()
        created_id = user.id
        return jsonify({'message': 'User added successfully.', 'data': {'id': created_id}}), 201
    except IntegrityError as ie:
        db.session.rollback()
        return jsonify({'error': 'Username or email already exists.', 'details': str(ie)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to add user.', 'details': str(e)}), 500


@app.route('/dashboard')
@login_required
def dashboard():
    return f'Hello, {current_user.login}! This is secure page'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    def check_password(self, password):
        print(self.password_hash)
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def __init__(self, login1, password):
        self.login = login1
        self.set_password(password)


@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = Employees.query.get(employee_id)
    if employee:
        return jsonify({
            'code': 200,
            'result': 'success',
            'data': employee.to_dict()
        })
    else:
        return jsonify({
            'result': 'error',
            'error': 'Resource not found',
            'data': None,
            'code': 404
        }), 404


@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employees.query.all()
    employee_list = [employee.to_dict() for employee in employees]
    return jsonify({
        'result': 'success',
        'data': employee_list
    })


@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    print(f'token: {token}')
    if not token:
        return jsonify({'message': 'Token is missing'}), 401

    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        user = Users.query.get(payload['user_id'])
        if not user:
            raise jwt.InvalidTokenError

        return jsonify({'message': 'You are authorized!'})

    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except (jwt.InvalidTokenError, jwt.DecodeError):
        return jsonify({'message': 'Invalid token'}), 401


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True, port=8080)
