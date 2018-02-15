#!/usr/bin/env python

import logging
import json

import connexion
from connexion import NoContent
from photo import Photo
from mongoengine import *
from bson.objectid import ObjectId
from bson import json_util
from bson.errors import InvalidId
import pymongo
from flask import jsonify
import json
import flask

from photo_mongo_wrapper import *

# See:
# https://devops.com/pymongo-pointers-make-robust-highly-available-mongo-queries
# for Robust Mongo Queries

def get_photos(offset, limit):
    try:
        ids = mongo_get_photos(offset, limit)
    except pymongo.errors.ServerSelectionTimeoutError as sste:
        return 503
    return json.loads(json.dumps(ids)) # is it necessary ?

def get_photo(photo_id):
    logging.debug('Getting photo with id: ' + photo_id)
    try:
        ph = mongo_get_photo(photo_id)
        ph._data.pop('id') # This is not very clean ...
    except (Photo.DoesNotExist, InvalidId) as e:
        return 'Not Found', 404
    except pymongo.errors.ServerSelectionTimeoutError as sste:
        return 'Mongo unavailable', 503
    return json.loads(json.dumps(ph._data, indent=4, default=json_util.default))

def post_photos(photo):                                           
    try:                                                                        
        if mongo_check(photo['author']) > 0:                       
            return 'Conflict', 409                                              
        else:                                                                   
            ph = mongo_add (photo['author'],                    
                            photo['filename'],
                            photo['b64'],
                            photo['tags'])                          
            return 'Created', 201, {'location': '/photo/' + str(ph.id)} 
    except pymongo.errors.ServerSelectionTimeoutError as sste:                  
        return 'Mongo unavailable', 503                                         

def delete_photo(photo_id):
    ph = Photo.objects(id=ObjectId(photo_id)).get().delete()
    return 'NoContent', 204

def put_photo(photo_id, photo):
    try:
        ph = mongo_get_photo(photo_id)
        ph['author'] = photo['author']
        ph['tags'] = photo['tags']
        ph['b64'] = photo['b64']
        ph['filename'] = photo['filename']
        ph.save()
    except (Photo.DoesNotExist, InvalidId) as e:
        return 'Not Found', 404
    return 'Modified', 201, {'location': '/photo/' + str(ph.id)} 
	
