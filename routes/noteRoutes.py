from flask import Blueprint, jsonify, request
from services.service import get_all_notes_service, get_note_by_id_service, create_note_service, update_note_service, delete_note_service


notes_bp = Blueprint('notes',__name__)

@notes_bp.route('/api/v1/notes', methods=['GET'])
def get_notes():
    notes = get_all_notes_service()
    notes_list = [{'id': note.id, 'name': note.name, 'description': note.description} for note in notes]
    return jsonify({'notes': notes_list})

@notes_bp.route('/api/v1/notes', methods=['POST'])
def create_notes():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    if not name or not description:
        return jsonify({"error": "Name and description are required"}), 400

    new_note = create_note_service(name, description)
    if new_note is None:
        return jsonify({"error": "Failed to create note"}), 500

    return jsonify({'message': 'note created successfully', 'note': new_note.id}), 201


@notes_bp.route('/api/v1/notes/<int:note_id>', methods=['GET'])
def get_notes_id_route(note_id):
        note = get_note_by_id_service(note_id)
        if note:
            return jsonify({'note': {'id': note.id, 'name': note.name, 'description': note.description}})
        else:
            return jsonify({'error': 'Note not found'}), 404
        


@notes_bp.route('/api/v1/notes/<int:note_id>', methods=['PUT'])
def update_notes_routes(note_id):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        
        if not name or not description:
            return jsonify({'error': 'Name and description are required'}), 400
        
        updated_note = update_note_service(note_id, name, description)
        
        if updated_note:
            return jsonify({'message': 'Note updated successfully', 'note': updated_note}), 200
        else:
            return jsonify({'error': 'Note not found'}), 404
        

@notes_bp.route('/api/v1/notes/<int:note_id>', methods=['DELETE'])
def delete_note_routes(note_id):
     existing_note = get_note_by_id_service(note_id)
     if existing_note:
          delete_note_service(note_id)
          return jsonify({'message': 'note deleted succesffully'})
     else:
          return jsonify({'error': 'note not found'}), 404
