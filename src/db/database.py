import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

#DATABASE_URL = 'postgresql://root:root@localhost/postgresql'
DATABASE_URL = 'postgresql://root:root@localhost/postgres'

engine = _sql.create_engine(DATABASE_URL)


SessionLocal = _orm.sessionmaker(autoflush=False,
                            autocommit=False,
                            bind=engine)


Base = _declarative.declarative_base()
