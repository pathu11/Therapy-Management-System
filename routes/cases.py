from flask import Blueprint, request, jsonify,session
from models import Case
from wrapper import token_required
cases_blueprint= Blueprint('cases', __name__)
cb= cases_blueprint

@cb.route('/cases', methods=['GET'])
@token_required
def get_cases():
    cases = Case.get_all_cases()
    return jsonify([dict(row) for row in cases])

@cb.route('/case', methods=['POST'])
@token_required
def add_case():
    data = request.json
    name, description = data.get('name'), data.get('description')
    if not name:
        return jsonify({'error': 'Case name is required!'}), 400
    Case.add_case(name, description)
    return jsonify({'message': 'Case added successfully!'})
