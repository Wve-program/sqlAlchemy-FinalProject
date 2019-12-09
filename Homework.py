#This is the tutorial coding used for the Homework and tested separately between here and pycharm

from sqlalchemy.orm import sessionmaker, Session
Session = sessionmaker(bind=engine)

session = Session()

c1 = Customer(first_name = 'Jane', 
              last_name = 'Doe', 
              username = 'JDoe', 
              email = 'janedoe01@aol.com', 
              address = '152 West Nyack Street',
              town = 'West Nyack'
             )
 
c2 = Customer(first_name = 'John', 
              last_name = 'Doe',
              username = 'JohnDoe',
              email = 'JohnDoe@aol.com
              address = 'West Nyack",
              town = 'West Nyack
             )
c1, c2

c1.first_name, c1.last_name
c2.first_name, c2.last_name
