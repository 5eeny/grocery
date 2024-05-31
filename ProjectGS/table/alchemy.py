import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import select

from sqlalchemy.orm import session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

class Author(Base):
    __tablename__= 'author'
    author_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    authors = relationship("User", secondary="author_user")

class Author_user(Base):
    __tablename__= 'author_user'
    auth_id = Column(Integer, ForeignKey("author.author_id"), primary_key=True, nullable=False )
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True, nullable=False )

engine = create_engine("sqlite:///./testdb.sqlite3")

if __name__=='__main__':
    stmt = select(User)
    print(stmt)
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(row)


