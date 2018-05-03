from program_note import database

def add_note(title, note, categories, uid):
    note = database.Notes(title=title, note=note, category=categories, user_id=uid)
    database.db.session.add(note)
    database.db.session.commit()