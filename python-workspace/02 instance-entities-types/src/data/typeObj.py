import datetime
import mongoengine


class TypeObj(mongoengine.Document):
    """This program intends to be manager of the columns,
        Instances and types of the table.
        *args =     typeObjUri
    """
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    typeObjUri = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'typeObj'
    }
