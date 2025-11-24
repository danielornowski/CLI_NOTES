from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

engine = create_engine('sqlite:///data/notes.db', echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Note(Base): 
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(200), nullable=False)
    timestamp = Column(String(50), nullable=False)

Base.metadata.create_all(bind=engine)


def add_note_to_db(text: str):
    db = SessionLocal()
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_note = Note(text=text, timestamp = now)
        db.add(new_note)
        db.commit()
        db.refresh(new_note)
        return new_note
    except Exception as e:
        db.rollback()
        print("Database error while adding note:", e)
        return None
    finally:
        db.close()

def get_all_notes():
    db = SessionLocal()
    try:
        notes = db.query(Note).all()
        return notes
    finally: 
        db.close()

def get_note_by_id(note_id: int):
    db = SessionLocal()
    try:
        return db.query(Note).filter(Note.id == note_id).first()
    finally:
        db.close()

def update_note_db(note_id: int, new_text: str):
    db = SessionLocal()
    try:
        note = db.query(Note).filter(Note.id == note_id).first()

        if note is None:
            print("Note not found.")
            return None
        
        note.text = new_text
        note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        db.commit()
        db.refresh(note)
        return note
    except Exception as e:
        db.rollback()
        print("Database error while updating", e)
        return None
    finally:
        db.close()

def delete_note_db(note_id):
    db = SessionLocal()
    try:
        note = db.query(Note).filter(Note.id == note_id).first()

        if note is None:
            print("Note not found.")
            return False
        
        db.delete(note)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print("Database error while deleting", e)
        return False 
    finally:
        db.close()

