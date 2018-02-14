from mongoengine import *

class Photo(Document):
    author = StringField(max_length=120, required=True)
    filename = StringField(max_length=120, required=True)
    b64 = StringField(max_length=120, required=True)  
    tags = ListField(StringField(max_length=30))
    
