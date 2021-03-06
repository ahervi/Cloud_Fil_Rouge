#!/usr/bin/env python
from flask import Flask
from flask_cors import CORS, cross_origin
import socket
app = Flask(__name__)
ip_addr_photographer = "photographer"
ip_addr_photo = "photo"
photographer_app_port = "8090"
photo_app_port = "8091"

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/photographer')
@cross_origin()
def index():

    res = "Define photographer:<br/>"
    res += "<form id='photographer_form' method='post' action='http://"+socket.gethostbyname(ip_addr_photographer)+":"+ photographer_app_port + "/photographers'>"
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

@app.route('/photo')
@cross_origin()

def index2():
    res = "Define photo:<br/>"
    res += "<form id='photo_form' method='post' action='http://"+socket.gethostbyname(ip_addr_photo)+":"+ photo_app_port + "/photos'>"
    res += "author:<br/><input type='test' name='author' id='author_input'><br/>"
    res += "filename:<br/><input type='test'name='filename' id='filename_input'><br/>"
    res += "tags:<br/><input name='tags' id='tags_input_1'><br/>"
    res += "<input name='tags' id='tags_input_2'><br/>"
    res += "<input name='tags' id='tags_input_3'><br/>"
    res += "b64:<br/><input type='file'name='b64' d='b64_input'><br/><br/>"
    res += "<input type='submit' value='Submit' id='photo_form_submit'>"
    res += "</form>"
    res += "<script type=\"text/javascript\" src=static/photoForm2Json.js></script>"
    return res


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')
