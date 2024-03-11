from sqlalchemy import create_engine, Column, Integer, String, text
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,declarative_base

# Define the database connection
engine = create_engine('sqlite:///example333.db')

# Define the base class for declarative class definitions
Base = declarative_base()

# Define your domain model (pedantic object)
class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()

# Execute the raw SQL query and map the results to Person objects
result_set = session.execute(text('SELECT id, name, age FROM person'))
people = [Person(id=row[0], name=row[1], age=row[2]) for row in result_set]

# Close the session
session.close()

# Now you can work with the list of Person objects
for person in people:
    print(person.id, person.name, person.age)


# session=Session()
# for i in range(20):
#     p=Person(id=i, name='person '+str(i), age=i*10)
#     session.add(p)
#     session.commit()
# session.close()