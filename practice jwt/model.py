from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from view import tweet as tweetview
from view import user as userview

Base = declarative_base()
class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

class followers_mapping(Base):
    __tablename__ = 'followers_mapping'
    id = Column(Integer, primary_key=True)
    user = Column(String)
    follow = Column(String)


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
        print(result)
        db.close()
        return result
    except:
        print("couldn't connect to DB")

def addObjectToDB(obj):
    try:
        db = Session()
        db.add(obj)
        db.commit()
        db.close()
        return True
    except:
        print("couldn't add obj to db")

    return False
def getNewsFeedData(username):
    # data = rawQuery(f"SELECT * FROM tweets where tweets.user in ( select follow from followers_mapping where user=(select id from user where name{username}))")
    data = rawQuery(f"SELECT * FROM tweets where tweets.user in ( select follow from followers_mapping where user=(select id from user where name={username}))")
    print(data)
    if data == None :
        return []
    dataToJson=[tweetview(*i).dict() for i in data]
    return dataToJson

print(getNewsFeedData('sharior'))


def follow(username,user_id ):
    user_id = rawQuery(f'select id from user where id={user_id}')
    current_id = rawQuery(f'select id from user where id={username}')
    if user_id and current_id:
        newfollowmapping = followers_mapping(user = user_id,follow = current_id )
        addObjectToDB(newfollowmapping)
    else:
        return 'invalid request'

    return None


def search(search):
    data= rawQuery(f'select * from user where name={search}')
    tweetdata= rawQuery(f'select * from tweet where text like %{search}%')
    if data == None and tweetdata == None :
        return []
    dataToJson=[userview(*i).dict() for i in data]
    tweets=[]
    for i in tweetdata:
        tweets.append(tweetview(*i).dict())
    return {'tweets':tweets,'user':dataToJson}


def insertUser(username, hashed_password):
    usr = user(username=username,password = hashed_password)
    addObjectToDB(usr)
    return None


def searchUser(username):
    return rawQuery(f'select * from user where name={username}')