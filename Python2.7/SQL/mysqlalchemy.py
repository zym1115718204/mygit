#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey

#创建对象的类
Base=declarative_base()

#define User object
class User(Base):

    #table name
    __tablename__='user'

    #table structure
    id=Column(String(20),primary_key=True)
    name=Column(String(20))

     # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))


#init sqldb:'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:88502355@localhost:3306/test')
DBSession=sessionmaker(bind=engine)

#向表中添加一项纪录
'''
session=DBSession()
new_user=User(id='4',name='4Michael')
session.add(new_user)
session.commit()
session.close()
'''
#查询记录
session=DBSession()
user=session.query(User).filter(User.id=='4').one()
#打印记录
print 'type:',type(user)
print 'name:',user.name

session.close()