#!/usr/bin/env python

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from pygen.tagThrift import TagThrift


try:
    transport = TSocket.TSocket('localhost', 30303)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = TagThrift.Client(protocol)
    transport.open()
    client.addTag("test")
    client.deleteTag("test")
    client.getTags("tes")
    transport.close()

except Thrift.TException as tx:
    print(tx.message)
