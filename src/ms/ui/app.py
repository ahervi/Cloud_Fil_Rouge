#!/usr/bin/env python
from flask import Flask
import connexion
from flask_cors import CORS, cross_origin

app = Flask(__name__)
ip_addr = "172.17.0.2"
photographers_app_port = "8090"
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():

	res = "Define photographer:<br/>"
	res += "<form id='photographer_form' method='post' action='http://"+ip_addr+":8090/photographers'>"
	res += "First name:<br/><input type='test' name='first_name' id='first_name_input'><br/>"
	res += "Display name:<br/><input type='test'name='display_name' id='display_name_input'><br/>"
	res += "Interests:<br/><input name='interests' id='interests_input_1'><br/>"
	res += "<input name='interests' id='interests_input_2'><br/>"
	res += "<input name='interests' id='interests_input_3'><br/>"
	res += "Last name:<br/><input type='test'name='last_name' d='last_name_input'><br/><br/>"
	res += "<input type='submit' value='Submit' id='photographer_form_submit'>"
	res += "</form>"
	res += "<script type=\"text/javascript\" src=static/input2json.js></script>"
	return res


if __name__ == '__main__':
    app.run(debug=True)
