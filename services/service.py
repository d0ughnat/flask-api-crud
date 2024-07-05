from repository.noteRepository import get_all_notes, get_id_note, create_note, update_note, delete_note

def get_all_notes_service():
    return get_all_notes()

def get_note_by_id_service(note_id):
    return get_id_note(note_id)

def create_note_service(name, description):
    return create_note(name, description)

def update_note_service(note_id, name, description):
    return update_note(note_id, name, description)

def delete_note_service(note_id):
    return delete_note(note_id)