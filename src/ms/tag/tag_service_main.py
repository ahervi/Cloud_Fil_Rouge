#!/usr/bin/env python
import logging
import json

from mongoengine import *
from bson.objectid import ObjectId
from bson import json_util
from bson.errors import InvalidId
import pymongo
import json
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from pygen.tagThrift import TagThrift
from tag_mongo_wrapper import *
from tag import Tag

class TagThriftHandler:
    def __init__(self):
        self.log = {}
    
    def getTag(tag_id):
        logging.debug('Getting tag with id: ' + tag_id)
        try:
            tag = mongo_get_tag(tag_id)
            tag._data.pop('id') # This is not very clean ...
        except (Tag.DoesNotExist, InvalidId) as e:
            return ['Not Found', '404']
        except pymongo.errors.ServerSelectionTimeoutError as sste:
            return ['Mongo unavailable', '503']
        return ['Get Ok', '201', tag['name']]

    def addTag(self, name):
        try:                                                                        
            if mongo_check(name) > 0:                       
                return ['Conflict', '409']                                              
            else:
                tag = mongo_add(name)                          
                return ['Created', '201', str(tag.id)]
        except pymongo.errors.ServerSelectionTimeoutError as sste:                  
            return ['Mongo unavailable', '503']  

    def getTags(self, beginTag):
        return mongo_get_begin_tags(beginTag)

    def deleteTag(self, tag_id):
        tag = Tag.objects(id=ObjectId(tag_id)).get().delete()
        return ['NoContent', '204']

    def deleteAllTags(self):
        Tag.objects.all().delete()
	return





logging.basicConfig(level=logging.DEBUG)

#connect("mongodb://user:pwd@mongodb_photographer:27017/photographers", alias="photographers")
connect("tags", host="127.0.0.1")
# from http://coderobot.downley.net/swagger-driven-testing-in-python.html
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app


if __name__ == '__main__':




    handler = TagThriftHandler()
    processor = TagThrift.Processor(handler)
    transport = TSocket.TServerSocket(port=30303)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print("Starting tag server...")
    server.serve()
    print("done!")
