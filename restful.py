from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name': 'Python'}, {'name': 'Javascript'}, {'name': 'Java'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message': 'it works'})

@app.route('/lang', methods=['GET'])
def returnall():
	return jsonify({'languages' : languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnone(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language': langs[0]})

@app.route('/lang', methods=['POST'])
def addone():
	language = {'name' : request.json['name']}
	languages.append(language)

	return jsonify({'languages': languages})

@app.route('/lang/<string:name>', methods=['PUT'])
def editone(name):
	langs = [language for language in languages if language['name'] == name]
	langs[0]['name'] = request.json['name']
	return jsonify({'language': langs[0]})


if __name__=='__main__':
	app.run(debug=True, port=8080)