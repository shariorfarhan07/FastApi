from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

class followers_mapping(Base):
    __tablename__ = 'followers_mapping'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

class tweet(Base):
    __tablename__ ='tweet'
    id = Column(Integer,primary_key=True)
    user = Column(Integer)
    text = Column(String)


engine = create_engine('sqlite:///test.db',echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)


def rawQuery(raw):
    try:
        db = Session()
        result = db.execute(text(raw))
        db.close()
        return result
    except:
        print("couldn't connect to DB")


