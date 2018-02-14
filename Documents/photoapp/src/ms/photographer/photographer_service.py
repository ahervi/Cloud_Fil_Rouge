#!/usr/bin/env python3

import logging
import json

import connexion
from connexion import NoContent
from photographer import Photographer
from mongoengine import *
from bson.objectid import ObjectId
from bson import json_util
from bson.errors import InvalidId
import pymongo
from flask import jsonify
import json
import flask

from photographer_mongo_wrapper import *

# See:
# https://devops.com/pymongo-pointers-make-robust-highly-available-mongo-queries
# for Robust Mongo Queries

def get_photographers(offset, limit):
    try:
        ids = mongo_get_photographers(offset, limit)
    except pymongo.errors.ServerSelectionTimeoutError as sste:
        return 503
    return json.loads(json.dumps(ids)) # is it necessary ?

def get_photographer(photographer_id):
    logging.debug('Getting photographer with id: ' + photographer_id)
    try:
        ph = mongo_get_photographer(photographer_id)
        ph._data.pop('id') # This is not very clean ...
    except (Photographer.DoesNotExist, InvalidId) as e:
        return 'Not Found', 404
    except pymongo.errors.ServerSelectionTimeoutError as sste:
        return 'Mongo unavailable', 503
    return json.loads(json.dumps(ph._data, indent=4, default=json_util.default))

def post_photographers(photographer):                                           
    try:                                                                        
        if mongo_check(photographer['display_name']) > 0:                       
            return 'Conflict', 409                                              
        else:                                                                   
            ph = mongo_add (photographer['display_name'],                       
                            photographer['first_name'],                         
                            photographer['last_name'],                          
                            photographer['interests'])                          
            return 'Created', 201, {'location': '/photographer/' + str(ph.id)} 
    except pymongo.errors.ServerSelectionTimeoutError as sste:                  
        return 'Mongo unavailable', 503                                         

def delete_photographer(photographer_id):
    ph = Photographer.objects(id=ObjectId(photographer_id)).get().delete()
    return 'NoContent', 204

def put_photographer(photographer_id, photographer):
    try:
        ph = mongo_get_photographer(photographer_id)
        ph['last_name'] = photographer['last_name']
        ph['display_name'] = photographer['display_name']
        ph['first_name'] = photographer['first_name']
        ph['interests'] = photographer['interests']
        ph.save()
    except (Photographer.DoesNotExist, InvalidId) as e:
        return 'Not Found', 404
    return 'Modified', 201, {'location': '/photographer/' + str(ph.id)} 
	