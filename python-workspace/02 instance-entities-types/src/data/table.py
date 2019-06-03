import datetime
import mongoengine

from data.column import Column


class Table(mongoengine.Document):
    """ this is the entity object that contains
        *args:
                name: str
                columns: {columnId : column}
    """
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    columns = mongoengine.EmbeddedDocumentListField(Column)

    meta = {
        'db_alias': 'core',
        'collection': 'table'
    }