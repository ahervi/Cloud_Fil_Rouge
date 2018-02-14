import pytest
import connexion
import json
from bson import json_util
import logging

#logging.basicConfig(level=logging.DEBUG)

@pytest.mark.usefixtures("clearTags")
@pytest.mark.usefixtures("initDB")
class TestClass(object):

    data1 = {'name': 'rdoisneau'}

    data2 = {'name': 'Tarzan'}

    headers_content = {'Content-Type': 'application/json'}
    headers_accept  = {'Accept': 'application/json'}

    @staticmethod
    def test_add_once(client):
        assert client.addTag("ts") == True
    
    @staticmethod
    def test_add_delete(client):
        assert client.addTag("ts") == True
        assert client.deleteTag("ts") == "ts"
