import data.mongo_setup as mongo_setup
import classes.table_annotation as table_annotation


def run():
    mongo_setup.global_init()

    try:
        table_annotation.run()
    except KeyboardInterrupt:
        return

run()