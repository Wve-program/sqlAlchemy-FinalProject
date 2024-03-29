#This is the tutorial code used for the Homework and tested separately between here and pycharm
#Step 1
from sqlalchemy.orm import sessionmaker, Session
Session = sessionmaker(bind=engine)

session = Session()

#End of Step 1

#Step 2
c1 = Customer(first_name = 'Jane', 
              last_name = 'Doe', 
              username = 'JDoe', 
              email = 'janedoe01@aol.com', 
              address = '152 West Nyack Street',
              town = 'West Nyack')
 
c2 = Customer(first_name = 'John', 
              last_name = 'Doe',
              username = 'JohnDoe',
              email = 'JohnDoe@aol.com
              address = 'West Nyack",
              town = 'West Nyack')
c1, c2

c1.first_name, c1.last_name
c2.first_name, c2.last_name

#Step 2 continuing, added objects, but now to call them.

session.add(c1)
session.add(c2)

#adding changes and objects to the session

session.add_all([c1, c2])
session.commit()

#End of Step 2, The point of step two is defining the data put in the session.
#Using c1.id can call and display an output message of what C1 is defined as. 

#Step 3, Query Data

session.query(Customer).all()
#Output: Displays Jane and John Doe's name

q = session.query(Customer)
 
for c in q:
    print(c.id, c.first_name)
    
#Using above code, will only yield the First name of the customers. 
#After Going through Tutorial part of data querying, it's mainly fetching and narrowing data searching. 
#All outputs have been good up to this point. End of Step 3

#Step 4. recreating the session I used the tutorial code for dealing with duplicates.
from sqlalchemy import distinct
 
session.query(Customer.town).filter(Customer.id  < 10).all()
session.query(Customer.town).filter(Customer.id  < 10).distinct().all()
 
session.query(        
    func.count(distinct(Customer.town)),
    func.count(Customer.town)
).all()

#This only yielded objects 1 and 2, due to me only putting two objects in there.

#Using session Union command wouldn't work, because I never defined items.

#Step 5 using Updating code
i = session.query(Customer).get(1)
i.name_change = Jonathan
session.add(i)
session.commit()

#Using the session.add(i) and session.commit() stages and saves my changes similar to docker

i = session.query(Customer).filter(customer.name == 'JohnDoe').one()
i
session.delete(i)
session.commit()

#Step 6 Using the Delete command above I could remove the name John Doe. Correction using "Customer.username =" I removed JohnDoe


