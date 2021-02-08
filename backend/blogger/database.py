import shelve
from typing import Any, Dict
from uuid import UUID, uuid4


class Database:
    def __init__(self, filename="shelve.db"):
        self.filename = filename

    def create(self, item: Any) -> UUID:
        with shelve.open(self.filename) as db:
            uuid = uuid4()
            db[uuid] = item
            return uuid

    def read(self, uuid: UUID) -> Any:
        with shelve.open(self.filename) as db:
            return db[uuid]

    def update(self, uuid: UUID, item: Any):
        with shelve.open(self.filename) as db:
            db[uuid] = item

    def delete(self, uuid: UUID):
        with shelve.open(self.filename) as db:
            db.pop(uuid)
