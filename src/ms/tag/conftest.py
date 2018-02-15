import pytest
from mongoengine import connect
from tag import Tag
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from pygen.tagThrift import TagThrift

@pytest.fixture(scope="class")
def client():
    try:
        transport = TSocket.TSocket('localhost', 30303)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = TagThrift.Client(protocol)
        transport.open()
        yield client
    except Thrift.TException as tx:
        print(tx.message)


@pytest.fixture
def clearTags():

    Tag.objects.all().delete()


    
@pytest.fixture(scope="class")
def initDB():
    connect("tags_test", host="127.0.0.1")
    yield
    # add code to destroy the database ?
