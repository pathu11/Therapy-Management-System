from flask import Blueprint, request, jsonify,session
from models.models import Case
from utils.wrapper import token_required
from utils.jwt_util import get_user_id_from_header

cases_blueprint= Blueprint('cases', __name__)
cb= cases_blueprint

@cb.route('/cases', methods=['GET'])
# @token_required
def get_cases():
    cases = Case.get_all_cases()
    return jsonify([dict(row) for row in cases])

@cb.route('/case', methods=['POST'])
@token_required
def add_case():
    try:
        userid = get_user_id_from_header()
    except ValueError as e:
        return jsonify({'error': str(e)}), 403
    
    data = request.json
    name, description = data.get('name'), data.get('description')

    if not name :
        return jsonify({'error': 'Case name  is required!'}), 400
    Case.add_case(userid,name, description)
    
    return jsonify({'message': 'Case added successfully!'}), 200

@cb.route('/case/<int:case_id>', methods=['DELETE'])
@token_required
def delete_case(case_id):
    try:
        logged_in_user_id = get_user_id_from_header()
    except ValueError as e:
        return jsonify({'error': str(e)}), 403
    case = Case.get_case_by_id(case_id)

    if not case:
        return jsonify({'error': 'Case not found!'}), 404

    if case['userid'] != logged_in_user_id:
        return jsonify({'error': 'Unauthorized to delete this case!'}), 403

    Case.delete_case(case_id)
    return jsonify({'message': 'Case deleted successfully!'}), 200

