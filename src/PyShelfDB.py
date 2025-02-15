import json


class PyShelfDB:
    def __init__(self, file_path="db.json") -> None:
        self.file_path = file_path

    def load_data(self) -> None:
        try:
            with open(self.file_path, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []
            self.commit()

    def commit(self) -> None:
        with open(self.file_path, "w") as file:
            json.dump(self.data, file)

    def insert(self, record:dict):
        self.data.append(record)
        self.commit()

    def filter(self, **kwargs) -> list:
        return [record for record in self.data if all(record.get(k) == v for k, v in kwargs.items())]

    def update(self, filter_func, update_func):
        for record in self.data:
            if filter_func(record):
                update_func(record)
        self.commit()

    def delete(self, filter_func):
        self.data = [record for record in self.data if not filter_func(record)]
        self.commit()
