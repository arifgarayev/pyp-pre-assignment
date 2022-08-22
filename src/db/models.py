import datetime as _dt
import sqlalchemy as _sql

import src.db.database as _database

class Contact(_database.Base):
    __tablename__ = 'data'
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
