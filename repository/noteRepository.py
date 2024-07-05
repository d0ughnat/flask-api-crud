import psycopg2

from models.note import Note

def deb_conn():
    return psycopg2.connect(dbname="crud", user="nat", password="123", host="localhost", port="5432")

def get_all_notes():
    conn = deb_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM schema.crudTutorial''')
    notes = cur.fetchall()
    cur.close()
    conn.close()

    notes = [Note(id=note[0], name=note[1], description=note[2]) for note in notes]
    return notes

def get_id_note(note_id):
    conn = deb_conn()  
    cur = conn.cursor()
    cur.execute('''SELECT * FROM schema.crudTutorial WHERE id = %s''', (note_id,))
    note_data = cur.fetchone()
    cur.close()
    conn.close()

    if note_data:
        return Note(id=note_data[0], name=note_data[1], description=note_data[2])
    else: 
        return None

def create_note(name, description):
    conn = deb_conn()
    cur = conn.cursor()
    try:
        cur.execute('''INSERT INTO schema.crudTutorial (name, description) VALUES (%s, %s) RETURNING id;''', (name, description))
        
        result = cur.fetchone()
        if result is None:
            raise Exception("No ID returned after INSERT")
        
        new_note_id = result[0]
        conn.commit()
        
    except Exception as e:
        conn.rollback()
        print(f"Error creating note: {e}")
        return None
    
    finally:
        cur.close()
        conn.close()
    
    return Note(new_note_id, name, description)



def update_note(note_id, name, description):
    conn = deb_conn()  
    cur = conn.cursor()
    cur.execute('''UPDATE schema.crudTutorial
                   SET name = %s, description = %s
                   WHERE id = %s RETURNING id, name, description''',
                (name, description, note_id))
    updated_note = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if updated_note:
        return {'id': updated_note[0], 'name': updated_note[1], 'description': updated_note[2]}
    else:
        return None


def delete_note(note_id):
    conn = deb_conn()  
    cur = conn.cursor()
    cur.execute('''DELETE FROM schema.crudTutorial WHERE id = %s''', (note_id,))
    conn.commit()
    cur.close()
    conn.close()
