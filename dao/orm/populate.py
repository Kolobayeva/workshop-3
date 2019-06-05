from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormUser).delete()
session.query(ormMessage).delete()
session.query(ormBoard).delete()

# populate database with new rows

Bob = ormUser( user_name="Bob",
               user_email='bob@gmail.com',
               user_phone='0966815412',
               )



Boba = ormUser( user_name="Bob",
               user_email='bob@gmail.com',
               user_phone='0966815412',
               )


Boban = ormUser( user_name="Bob",
               user_email='bob@gmail.com',
               user_phone='0966815412',
               )



BobM = ormMessage(text_mes='Message1')
BobaM = ormMessage(text_mes='Message2')
BobanM = ormMessage(text_mes='Message22')

# create relations
Bob.orm_message.append(BobM)
Boba.orm_message.append(BobaM)

Boban.orm_message.append(BobanM)



# insert into database
session.add_all([BobM,BobaM,BobanM,Boba,Bob,Boban])

session.commit()
