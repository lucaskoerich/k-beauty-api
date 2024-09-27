from flask import Blueprint, request, jsonify
from models import Procedure, db
procedures_bp = Blueprint('procedures', __name__)

@procedures_bp.route('/procedures', methods=['POST'])
def add_procedure():
    data = request.get_json()
    new_procedure = Procedure(name=data['name'], value=data['value'], duration=data['duration'])
    db.session.add(new_procedure)
    db.session.commit()
    return jsonify({'message': 'Procedure added successfully!'}), 201

@procedures_bp.route('/procedures', methods=['GET'])
def get_procedures():
    procedures = Procedure.query.all()
    return jsonify([{'id': procedure.id, 'name': procedure.name, 'value': str(procedure.value), 'duration': procedure.duration} for procedure in procedures]), 200

@procedures_bp.route('/procedures/<int:procedure_id>', methods=['DELETE'])
def delete_procedure(procedure_id):
    procedure = Procedure.query.get(procedure_id)
    if procedure is None:
        return jsonify({'message': 'Procedure not found!'}), 404
    
    db.session.delete(procedure)
    db.session.commit()
    return jsonify({'message': 'Procedure deleted successfully!'}), 200
