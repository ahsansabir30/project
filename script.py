from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///employee.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    permissions = relationship('Permission', backref='role')

class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)

role = Role(name='System Engineer')
session.add(role)
session.commit()

permission1 = Permission(name='Internet Access', role=role)
permission2 = Permission(name='Email', role=role)
permission3 = Permission(name='Tenable', role=role)
permission4 = Permission(name='Azure', role=role)
session.add_all([permission1, permission2, permission3, permission4])
session.commit()

print('Role and permissions added successfully.')
