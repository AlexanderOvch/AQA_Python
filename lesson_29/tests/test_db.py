import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import db

def test_crud():
    db.init_db()

    db.insert_user("Oleksandr")
    users = db.get_users()
    assert len(users) == 1 and users[0][1] == "Oleksandr"

    db.update_user(users[0][0], "Sasha")
    updated = db.get_users()
    assert updated[0][1] == "Sasha"

    db.delete_user(users[0][0])
    assert db.get_users() == []
