from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

engine = create_engine('sqlite:///data/notes.db')

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Note(Base): 
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    text = Column(String(50))
    timestamp = Column(String(50))

Base.metadata.create_all(bind=engine)


def add_note_to_db(text):
    db = SessionLocal()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_note = Note(text=text, timestamp = now)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    db.close()
    return new_note

def get_all_notes():
    db = SessionLocal()
    notes = db.query(Note).all()
    db.close()
    return notes