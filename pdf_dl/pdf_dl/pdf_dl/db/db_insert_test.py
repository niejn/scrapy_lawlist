from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapper, create_session
from sqlalchemy import create_engine, Column, Integer, Sequence, DateTime, String, Numeric, func, Text
from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
# Base = declarative_base()
engine = create_engine('sqlite:///ann_spiders.sqlite', echo=True)
metadata = MetaData(bind=engine)
# class Announce(Base):
#     __table__ = Table('announcement', metadata, autoload=True)
class User(object):
    def __init__(self, title):
        self.title = title
users = Table('announcement', metadata, autoload=True)
usermapper = mapper(User, users)
# session = create_session(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(User)
print(query)  # 显示SQL 语句
print(query.statement)  # 同上
for user in query:  # 遍历时查询
    print(user.title)

add_user = User(title='add1')
session.add(add_user)
# d_acc = Announce(title='papapa')
#
# session.add(d_acc)
session.commit()
session.close()
'''
from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base

#Create and engine and get the metadata
Base = declarative_base()
engine = create_engine('put your database connect string here')
metadata = MetaData(bind=engine)

#Reflect each database table we need to use, using metadata
class Tests(Base):
    __table__ = Table('Tests', metadata, autoload=True)

class Users(Base):
    __table__ = Table('Users', metadata, autoload=True)

#Create a session to use the tables    
session = create_session(bind=engine)

#Here I will just query some data using my foreign key relation,  as you would
#normally do if you had created a declarative data mode.
#Note that not all test records have an author so I need to accomodate for Null records
testlist = session.query(Tests).all()    

for test in testlist:
    testauthor = session.query(Users).filter_by(id=test.author_id).first()  
    if not testauthor:
        print "Test Name: {}, No author recorded".format(test.testname)
    else:
        print "Test Name: {}, Test Author: {}".format(test.testname, testauthor.fullname)

'''