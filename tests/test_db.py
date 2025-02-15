from src.PyShelfDB import PyShelfDB

db = PyShelfDB()

db.load_data()

new_record = {
    "id": 1,
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

db.insert(new_record)