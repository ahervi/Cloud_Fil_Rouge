#!/usr/bin/env python3

import logging
import json

import connexion
from connexion import NoContent
from tag import Tag
from mongoengine import *

from bson.objectid import ObjectId
from bson import json_util
from bson.errors import InvalidId

import json
import robustify

@robustify.retry_mongo
def mongo_check(name):
    count = Tag.objects(name=name).count()
    return count

@robustify.retry_mongo
def mongo_add(display_name, first_name, last_name, interests):
    t = Tag(display_name = display_name,
                      first_name = first_name,
                      last_name = last_name,
                      interests = interests).save()
    return t

@robustify.retry_mongo
def mongo_get_tag(tag_id):
    t = Tag.objects(id=ObjectId(tag_id)).get()
    return t
