from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine('mysql+pymysql://root:ailuoli@localhost:3306/fortress_server', echo=True)
base = declarative_base()

class BindHost(base):

    __tablename__ = 'bindhost'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True, nullable=False)
    host = Column(String(32), unique=True, nullable=False)
    ip = Column(String(15), unique=True, primary_key=True, nullable=False)

class User(base):

    __tablename__ = 'user'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(8), unique=True, primary_key=True, nullable=False)
    password = Column(String(16), default='dev123.A')

    def __repr__(self):
        return "<UserProfile(id='%s',username='%s')>" % (self.id,self.username)

class Gourp(base):

    __tablename__ = 'gourp'
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True, nullable=False)
    gourpname = Column(String(8), unique=True, primary_key=True, nullable=False)
    # attribute = Column(String(8))

    def __repr__(self):
        return "<UserProfile(id='%s',username='%s')>" % (self.id, self.gourpname)

# class User2Gourp(base):
#
#     __tablename__ = 'user2gourp'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, primary_key=True)
#     gourp_id = Column(String(255))
#
#
# class Gourp2BindHost(base):
#     pass

if __name__ == "__main__":
    base.metadata.create_all(db)
    # Session = sessionmaker(bind=db)
    # session = Session()
    # ed_user = User(username='ed',password='alex123')
    # session.add(ed_user)
    # session.commit()