import mongoengine


def global_init():
    mongoengine.register_connection(alias='core', name='tables_schema_annotation')
