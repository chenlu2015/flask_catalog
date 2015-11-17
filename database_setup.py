#db configuration 
import sys
from sqlalchemy import Column, ForeignKey, Integer, Float, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

#class definitions
class Category(Base):
	__tablename__ = 'categories'
	name = Column(String(90), nullable = False)
	description = Column(String(255))
	id = Column(Integer, primary_key = True)

	def serialize(self):
    	#Returns object data in easily serializable format.
	    return {
	        'name': self.name,
	        'id': self.id,
	        'description': self.description,
	    }

class User(Base):
	__tablename__ = 'users'
	name = Column(String(90), nullable = False)
	email = Column(String(50))
	phone_number = Column(String(20))
	id = Column(Integer, primary_key = True)

class CatalogItem(Base):
	__tablename__ = 'catalog_item'
	id = Column(Integer, primary_key = True)
	name = Column(String(90), nullable = False)
	price = Column(Float, nullable = False)
	description = Column(String(255))
	category_id = Column(Integer, ForeignKey('categories.id'))
	owner_id = Column(Integer, ForeignKey('users.id'))
	category = relationship(Category)
	user = relationship(User)


#run db engine
engine = create_engine('postgresql+psycopg2://force:force@localhost/force')
Base.metadata.create_all(engine)