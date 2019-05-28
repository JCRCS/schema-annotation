import mongoengine
import datetime

class InstanceObj(mongoengine.EmbeddedDocument):
    """ this is the entity object that contains
        *args:
                table_id: Table.id
                column_id: Column.id
                text: str
    """
    table_id = mongoengine.ObjectIdField()
    column_id = mongoengine.ObjectIdField()

    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    text = mongoengine.StringField()
