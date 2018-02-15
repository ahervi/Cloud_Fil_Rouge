#!/usr/bin/env python

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from pygen.tagThrift import TagThrift


class TagThriftHandler:
    def __init__(self):
        self.log = {}
	
    def get_tag(tag_id):
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
                return 'Conflict', 409                                              
            else:                                                                   
                tag = mongo_add(name)                          
                return ['Created', '201', str(tag.id)]


    def deleteTag(self, tag_id):
        tag = Tag.objects(id=ObjectId(tag_id)).get().delete()
        return ['NoContent', '204']

    def getTags(self, beginTag):

        
        return mongo_get_begin_tags(beginTag)


handler = TagThriftHandler()
processor = TagThrift.Processor(handler)
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting tag server...")
server.serve()
print("done!")
