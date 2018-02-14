#!/usr/bin/env python

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from pygen.tagThrift import TagThrift


class TagThriftHandler:
    def __init__(self):
        self.log = {}

    def addTag(self, tag):
	#mogo db add tag to tag db
	print(tag)
        return True

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


handler = TagThriftHandler()
processor = TagThrift.Processor(handler)
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting tag server...")
server.serve()
print("done!")
