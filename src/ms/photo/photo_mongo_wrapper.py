#!/usr/bin/env python3

import logging
import json

import connexion
from connexion import NoContent
from photo import Photo
from mongoengine import *

from bson.objectid import ObjectId
from bson import json_util
from bson.errors import InvalidId

from flask import jsonify
import json
import flask
import robustify
import socket

@robustify.retry_mongo
def mongo_check(filename):
    count = Photo.objects(filename=filename).count()
    return count

@robustify.retry_mongo
def mongo_add(author, filename, b64, tags):
    ph = Photo(author = author, filename = filename, b64 = b64, tags = tags).save()
    return ph

@robustify.retry_mongo
def mongo_get_photos(offset, limit):
    qs = Photo.objects
    return [flask.request.url_root + "photo/" + str(ph.id)
            for ph in qs.order_by('id').skip(offset).limit(limit)]

@robustify.retry_mongo
def mongo_get_photo(photo_id):
    ph = Photo.objects(id=ObjectId(photo_id)).get()
    return ph
