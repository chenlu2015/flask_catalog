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

	def serialize(self):
    	#Returns object data in easily serializable format.
	    return {
	        'name': self.name,
	        'id': self.id,
	        'email': self.email,
	        'phone_number': self.phone_number
	    }

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

	def serialize(self):
    	#Returns object data in easily serializable format.
	    return {
	    	'id': self.id,
	        'name': self.name,
	   		'price': self.price,
	   		'description': self.description,
	   		'category_id': self.category_id,
	   		'owner_id': self.owner_id
	    }

#run db engine
engine = create_engine('postgresql+psycopg2://lolitschen:n5ryxcue@localhost/lolitschen')
Base.metadata.create_all(engine)