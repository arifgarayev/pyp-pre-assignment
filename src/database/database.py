import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from src.api.const import constants

engine = _sql.create_engine(constants.DATABASE_URL)


SessionLocal = _orm.sessionmaker(autoflush=False,
                            autocommit=False,
                            bind=engine)


Base = _declarative.declarative_base()
