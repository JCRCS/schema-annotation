import datetime
import mongoengine


class Entity(mongoengine.Document):
    """this is the entity object that contains
        *args:
                registered_date: datetime()
                text: stringField()
                type_ids = ListField()
    """
    instanceObj_id = mongoengine.ObjectIdField()

    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    entityUri = mongoengine.StringField(required=True)
    typeObj_ids = mongoengine.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'entity'
    }

