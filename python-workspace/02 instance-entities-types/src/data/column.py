import datetime
import mongoengine

from data.instanceObj import InstanceObj


class Column(mongoengine.EmbeddedDocument):
    """ this is the entity object that contains
        *args:
                table_id: Table.id
                name: str
                instances: []
    """
    table_id = mongoengine.ObjectIdField()

    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    
    instances = mongoengine.EmbeddedDocumentListField(InstanceObj)
