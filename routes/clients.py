from flask import Blueprint, request, jsonify
from models import Client, db

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    new_client = Client(name=data['name'], phone=data['phone'], gender=data['gender'])
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message': 'Client added successfully!'}), 201

@clients_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([{'id': client.id, 'name': client.name, 'phone': client.phone, 'gender': client.gender} for client in clients]), 200

@clients_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get(client_id)
    if client is None:
        return jsonify({'message': 'Client not found!'}), 404
    
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Client deleted successfully!'}), 200
