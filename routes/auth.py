from flask import Blueprint, request, jsonify
from models import Account, db 

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['POST'])
def add_login():
    data = request.get_json()

    # Verifica se o usuário já existe
    existing_user = Account.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'message': 'User already exists!'}), 409

    # Cria um novo usuário se não existir
    new_account = Account(name=data['name'], email=data['email'], password=Account.hash_password(data['password']))
    db.session.add(new_account)
    db.session.commit()
    return jsonify({'message': 'Account added successfully!'}), 201

@auth_bp.route('/accounts', methods=['GET'])
def get_accounts():
    accounts = Account.query.all()
    return jsonify([{'id': account.id, 'name': account.name, 'email': account.email} for account in accounts])

@auth_bp.route('/login', methods=['POST'])
def verify_login():
    data = request.get_json()
    user = Account.query.filter_by(email=data['email']).first()

    if user and Account.verify_password(user.password, data['password']):
        return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid username or password!'}), 401
