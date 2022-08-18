import datetime as _dt
import sqlalchemy as _sql

import database as _database

class XlsxData(_database.Base):
    def __init__(self, db_name: str):
        self.db_name: str = db_name

    def create_table(self):
        __tablename__ = str(self.db_name)

    id = _sql.Column(_sql.Integer, primary_key=True,
                     index=True)

