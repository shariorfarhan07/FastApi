from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

# Create an engine to connect to your database
engine = create_engine('sqlite:///example.db', echo=True)

# Create a base class for your declarative models
Base = declarative_base()

# Define your table classes by subclassing the Base class
class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password=Column(String)

class followers_mapping(Base):
    __tablename__ = 'followers_mapping'
    id = Column(Integer, primary_key=True)
    user=Column(Integer)
    follow=Column(Integer)

class tweets(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True)
    user = Column(Integer)
    text=Column(String)



# Create the tables in the database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
db = Session()

result = db.execute(text("SELECT * FROM tweets where tweets.user in ( select follow from followers_mapping where user=1)"))

for row in result:
    print(row)

db.close()