#!/usr/bin/env python

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from pygen.tag import Tag


class TagHandler:
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


handler = TagHandler()
processor = Tag.Processor(handler)
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting tag server...")
server.serve()
print("done!")
