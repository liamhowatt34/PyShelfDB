PyShelfDB

PyShelfDB is a lightweight JSON-based database system that provides basic CRUD (Create, Read, Update, Delete) operations. It allows users to store, filter, update, and delete records within a JSON file, making it a simple and efficient way to manage structured data without requiring a full database engine.

🚀 Features

Lightweight & Simple: No external dependencies beyond Python's built-in json module.

Persistent Storage: Data is stored in a JSON file (db.json by default).

Basic CRUD Operations: Insert, filter, update, and delete records with ease.

Flexible Querying: Filter records using key-value pairs.

📥 Installation

No installation is required. Simply include PyShelfDB.py in your project and import it.

📌 Usage

🔹 Initialization

from PyShelfDB import PyShelfDB

db = PyShelfDB("data.json")
db.load_data()

🔹 Inserting Data

record = {"id": 1, "name": "Alice", "age": 25}
db.insert(record)

🔹 Filtering Data

results = db.filter(name="Alice")
print(results)  # Outputs: [{"id": 1, "name": "Alice", "age": 25}]

🔹 Updating Data

def filter_func(record):
    return record["id"] == 1

def update_func(record):
    record["age"] = 26

db.update(filter_func, update_func)

🔹 Deleting Data

def filter_func(record):
    return record["id"] == 1

db.delete(filter_func)

📖 Methods Overview

Method

Description

__init__(file_path="db.json")

Initializes the database with the specified file path.

load_data()

Loads the database from the JSON file. If the file is not found, initializes an empty list.

commit()

Saves the current data state to the JSON file.

insert(record)

Inserts a new record into the database.

filter(**kwargs)

Filters records based on key-value conditions.

update(filter_func, update_func)

Updates records that match the filter_func condition using the update_func transformation.

delete(filter_func)

Deletes records that match the filter_func condition.

📜 License

This project is licensed under the MIT License.