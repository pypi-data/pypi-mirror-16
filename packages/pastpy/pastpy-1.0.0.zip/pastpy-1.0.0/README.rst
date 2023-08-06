pastpy - Python library for working with PastPerfect databases
==============================================================

Usage:

..

    from pastpy.object_dbf_table import ObjectDbfTable

    with ObjectDbfTable.open(dbf_file_path) as table:
        for object_ in table:
            print object_
