from flask import Flask, render_template, jsonify, abort, make_response, request
from flask.ext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

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

# REST API Routes
@app.route("/api/v1.0/categories", methods=['GET', 'POST'])
def get_categories():
	if request.method == 'GET':
		return jsonify({'categories': categories})
	elif request.method == 'POST':
		if not request.json or not 'name' in request.json:
			abort(400)
		category = {
			'id': categories[-1]['id'] +1,
			'name': request.json['name'],
			'description': request.json.get('description',"")
		}
		categories.append(category)
		return jsonify({'category': category}), 201

@app.route("/api/v1.0/categories/<int:category_id>", methods=['GET'])
def get_category(category_id):
	category = [category for category in categories if category['id']==category_id]
	if len(category) == 0:
		abort(404)
	return jsonify({'category':category[0]})

#error handling
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not Found'}), 404)

if __name__ == "__main__":
	app.run(host='localhost',port=8000)




