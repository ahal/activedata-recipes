"""
Get information on the ActiveData schema. The above command returns the
available tables. To see the columns in a table, run:

.. code-block:: bash

    adr inspect
    adr inspect --table task
"""
from __future__ import print_function, absolute_import

from ..query import run_query


def run(config, args):

    if not args.table:
        data = run_query('meta', config, args)['data']
        data = sorted([(d['name'],) for d in data])
        data.insert(0, ('Table',))
        return data

    if not args.attribute:
        data = run_query('meta_columns', config, args)['data']
        data = sorted([(d['name'],) for d in data])
        data.insert(0, ('Column',))
        return data

    data = run_query('meta_values', config, args)['data']
    data.insert(0, (args.attribute, 'count'))
    return data
