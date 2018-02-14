from mongoengine import *

class Tag(Document):
    name = StringField(max_length=120, required=True)
