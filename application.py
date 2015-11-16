from flask import Flask, render_template, jsonify
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

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/api/v1.0/categories", methods=['GET'])
def get_categories():
	return jsonify({'categories': categories})

if __name__ == "__main__":
	app.run(host='localhost',port=8000)





