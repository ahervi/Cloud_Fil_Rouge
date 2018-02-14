#!/usr/bin/env python

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
import logging
import connexion
from connexion import NoContent
from mongoengine import connect
from pygen.tagThrift import TagThrift

class TagThriftHandler:
    def __init__(self):
        self.log = {}

    def addTag(self, tag):
	#mogo db add tag to tag db
	print(tag)
        return

    def deleteTag(self, tag):
	#mogo db delete tag in tag db
	print(tag)
	return tag

    def getTags(self, beginTag):
        #mongo db get tags that begin with beginTag
        print(beginTag)
        tags = ["example1", "example2"]
        print(str(tags))
        return tags

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
