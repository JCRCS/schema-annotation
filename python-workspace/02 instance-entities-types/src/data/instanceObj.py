import mongoengine
import datetime

class InstanceObj(mongoengine.EmbeddedDocument):
    """ this is the entity object that contains
        *args:
                table_id: Table.id
                column_id: Column.id
                id: str
                text: str
    """
    table_id = mongoengine.ObjectIdField()
    column_id = mongoengine.IntField()
    id = mongoengine.IntField()

    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    text = mongoengine.StringField()
    entityObjs_ids = mongoengine.ListField()
