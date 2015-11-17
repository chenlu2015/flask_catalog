from flask import Flask, render_template,url_for, jsonify, abort, redirect, make_response, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from database_setup import Base, Category, User, CatalogItem
from json import dumps

def to_json(model):
    """ Returns a JSON representation of an SQLAlchemy-backed object.
    """
    json = {}
    json['fields'] = {}
    json['pk'] = getattr(model, 'id')

    for col in model._sa_class_manager.mapper.mapped_table.columns:
        json['fields'][col.name] = getattr(model, col.name)

    return dumps([json])

app = Flask(__name__)
engine = create_engine('postgresql+psycopg2://force:force@localhost/force')
Base.metadata.bind = engine

categories = [
    {
        'id': 1,
        'name': u'Sports Equipment',
        'description': u'Equipment for all different kinds of sports.'
    },
    {
        'id': 2,
        'title': u'Computer Hardware',
        'description': u'All kinds of hardware for computers: PSU, GPU, CPU, SSD, HDD, etc.'
    }
]

#Application Routes
@app.route("/")
def main():
	return render_template('index.html')

# API Routes
@app.route("/api/v1.0/categories/", methods=['GET'])
def get_categories():
		DBSession = sessionmaker(bind = engine)
		session = DBSession()
		categories = session.query(Category).all()
		data = []
		for c in categories:
			print c
			data.append(c.serialize())

		#print data
		session.close()
		return jsonify({'categories':data})

@app.route("/api/v1.0/categories/new/", methods = ['GET', 'POST'])
def new_category():
	if request.method == 'POST':
		#print 'name' in request.form
		if not request.form or not 'name' in request.form:
			abort(400)
		newCategory = Category(name = request.form['name'], description=request.form.get('description',""))
		DBSession = sessionmaker(bind = engine)
		session = DBSession()
		session.add(newCategory)
		session.commit()
		session.close()
		#print 'closing session'
		return redirect(url_for('new_category'), code=302)
	elif request.method == 'GET':
		return render_template('new_category_form.html')
	else:
		abort(400)

@app.route("/api/v1.0/categories/<int:category_id>/", methods=['GET'])
def get_category(category_id):
	DBSession = sessionmaker(bind = engine)
	session = DBSession()
	try:
		result = session.query(Category).filter_by(id=category_id).one()
		return jsonify({'category':result.serialize()})
	except NoResultFound:
		abort(404)
	finally:
		session.close()
		#print 'closing session'
@app.route("/api/v1.0/categories/<int:category_id>/edit/", methods=['GET', 'POST'])
def edit_category(category_id):
	if request.method == 'GET':
		DBSession = sessionmaker(bind = engine)
		session = DBSession()
		try:
			result = session.query(Category).filter_by(id=category_id).one()
			return render_template('edit_category.html', category = result)
		except NoResultFound:
			abort(404)
		finally:
			session.close()
	elif request.method == 'POST':
		DBSession = sessionmaker(bind = engine)
		session = DBSession()
		try:
			result = session.query(Category).filter_by(id=category_id).one()
			result.name = request.form['name']
			result.description = request.form['description']
			session.add(result)
			session.commit()
			return redirect(url_for('get_category',category_id=category_id),code=302)
		except NoResultFound:
			abort(404)
		finally:
			session.close()

		return 'test'
	else:
		abort(400)

#error handling
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not Found'}), 404)

if __name__ == "__main__":
	app.debug = True
	app.run(host='localhost',port=8000)




