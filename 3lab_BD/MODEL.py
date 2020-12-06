import DATA
import time
import sqlalchemy
from psycopg2 import errors

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import select,Column, String, Integer, ForeignKey, DateTime, create_engine, ext, func

engine=create_engine('postgresql://postgres:1705@localhost:5432/library')#echo = True
Session =  sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class genry(Base):
    __tablename__ = "id_genry"

    id_genry = Column(Integer, primary_key=True)
    genry = Column(String)
    books = relationship("book")

    def __init__(self, genry):

        self.genry = [genry]



class book(Base):
    __tablename__= 'books'

    id_boooks = Column(Integer,primary_key=True)
    author = Column(String)
    name_book = Column(String)
    genry =Column(Integer, ForeignKey('id_genry.id_genry'))
    journal = relationship("journal")


    def __init__(self,author,name_book,genry):
        self.author = author
        self.name_book = name_book
        self.genry = genry






class readers(Base):

 __tablename__ = "readers"

 id_readers = Column(Integer, primary_key=True)
 name = Column(String)
 surname = Column(String)
 phone_number = Column(Integer)
 journal = relationship("journal")

 def __init__(self,name,surname,phone_number):
     self.name = name
     self.surname = surname
     self.phone_number = phone_number




class journal(Base):
 __tablename__ = "journal"

 id_records = Column(Integer, primary_key= True)

 id_readers = Column(Integer, ForeignKey('readers.id_readers'))

 id_books = Column(Integer,ForeignKey('books.id_boooks'))

 data_time = Column(DateTime)

 def __init__(self, id_readers,id_books,data_time ):
     self.id_books = id_books
     self.id_readers = id_readers
     self.data_time = data_time


def Insert(conn,cur,name_table,tmp):
    try:
        error_test = True
        for x in DATA.data:
            if x == name_table:
                error_test = False
        if   error_test:
            print("error")
            return 4
        if name_table == "books":
            if tmp[2].isdigit() and not tmp[0].isdigit() and not  tmp[1].isdigit() :
                session.add(book(tmp[0],tmp[1],tmp[2]))
            else :
                print("error")
                return -1
        elif name_table == "journal":
            if  not tmp[2].isalpha()  and tmp[0].isdigit():
                session.add(journal(tmp[0],tmp[1],tmp[2]))
            else :
                print("error")
                return -1
        elif name_table == "id_genry":
            session.add(genry(tmp[0]))
        elif name_table == "readers":
            session.add(readers(tmp[0],tmp[1],tmp[2]))
        else:
            print("Error")
            return 4
        session.commit()
    except (Exception,errors,BaseException):
        print("error")
        return -1

def DELL(conn,cur,name_table,id):
    try:
        error_test = True
        for x in DATA.data:
            if x == name_table:
                error_test = False
        if error_test:
            print("error")
            return 4


        if name_table == "books":
            sql_delete = session.query(book).filter_by(id_boooks=id).one()
            session.delete(sql_delete)
            session.commit()

        elif name_table == "journal":

             sql_delete  = session.query(journal).filter_by(id_records = id).one()
             session.delete(sql_delete)
             session.commit()
        elif name_table == "id_genry":

             sql_delete = session.query(genry).filter_by(id_genry = id).one()
             session.delete(sql_delete)
             session.commit()
        elif name_table == "readers":
            sql_delete = session.query(readers).filter_by(id_readers = id).one()
            session.delete(sql_delete)
            session.commit()
        else:
            print("Error")
            return 4

    except (Exception):
        print("error ")
        return





def Update(conn,cur,name_table,tmp):
    try:
        error_test = True
        for x in DATA.data:
            if x == name_table:
                error_test = False
        if (not tmp[-1].isdigit()):
            print("error")
            return 4

        if name_table == "books" and len(tmp) == 7 and not  tmp[0].isdigit() and not  tmp[1].isdigit() and  not tmp[2].isdigit() \
                and not  tmp[3].isdigit() and not tmp[4].isdigit() and tmp[5].isdigit():
            session.query(Base).filter_by(id_boooks=tmp[-1]).update({book.author: tmp[1], book.name_book: tmp[3], book.genry: tmp[5]})
            session.commit()
        elif name_table == "journal" and len(tmp) == 8 and tmp[0]== "id_readers"  and not  tmp[1].isdigit() and tmp[2] == "id_books"\
                and tmp[3].isdigit() and not tmp[4].isdigit():
            print(len(tmp))
            data_time = tmp[5] + " " + tmp[6]
            print(data_time.isdigit())
            if data_time.isdigit():
                session.query(journal).filter_by(id_records= tmp[-1]).update(
                    {journal.id_readers: tmp[1], journal.id_books: tmp[3], journal.data_time: data_time})
                session.commit()
            else:
                print("error")
                return 4
        elif name_table == "id_genry" and len(tmp) == 3 and tmp[0] == "genry" and not  tmp[1].isdigit() :
            session.query(genry).filter_by(id_genry=tmp[-1]).update(
                {genry.genry: tmp[1]})
            session.commit()
        elif name_table == "readers" and len(tmp) == 7 and tmp[0] == "name"and not tmp[1].isdigit() and tmp[2] == "surname" \
                and not tmp[3].isdigit() and tmp[4] == "phone_number" and tmp[5].isdigit() :
            session.query(readers).filter_by(id_readers=tmp[-1]).update(
                {readers.name: tmp[1], readers.surname: tmp[3], readers.phone_number: tmp[5]})
            session.commit()
        else:
            print("Error")
            return 4

    except (Exception,errors,BaseException):
        print("error 1 ")
        return



