import data.mongo_setup as mongo_setup
import classes.table_annotation as table_annotation
import classes.column_candidates as column_candidates
import classes.NEL.Nel as nel



def main():
    mongo_setup.global_init()

    try:
        table_annotation.run()
    except KeyboardInterrupt:
        return

main()