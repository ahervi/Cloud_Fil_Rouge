import pytest
import connexion
import json
from bson import json_util
import logging


#logging.basicConfig(level=logging.DEBUG)

@pytest.mark.usefixtures("clearTags")
@pytest.mark.usefixtures("initDB")
class TestClass(object):

    data1 = {'name': 'Tarzan'}

    data2 = {'name': 'Tarzanou'}
    
    data3 = {'name': 'Patate'}

    headers_content = {'Content-Type': 'application/json'}
    headers_accept  = {'Accept': 'application/json'}

    @staticmethod
    def test_add_delete(client):
        client.deleteAllTags()
        res = client.addTag(TestClass.data1['name'])
        assert res[1] == '201'
	res2 = client.deleteTag(res[2])
        assert res2[1] == '204'
    
    @staticmethod
    def test_add_once(client):
        client.deleteAllTags()
        res = client.addTag(TestClass.data1['name'])
        assert res[1] == '201'
    
    @staticmethod
    def test_add_twice(client):
        client.deleteAllTags()
        res = client.addTag(TestClass.data1['name'])
        assert res[1] == '201'
        res2 = client.addTag(TestClass.data1['name'])
        assert res2[1] == '409'

    @staticmethod
    def test_get_beginning(client):
        client.deleteAllTags()
        res = client.addTag(TestClass.data1['name'])
        assert res[1] == '201'
        res2 = client.addTag(TestClass.data2['name'])
        assert res2[1] == '201'
        res3 = client.getTags(TestClass.data1['name'])
        assert TestClass.data1['name'] in res3 and TestClass.data2['name'] in res3 and len(res3) == 2
        



