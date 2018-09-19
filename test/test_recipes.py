from __future__ import print_function, absolute_import

import json
import os
import sys
from imp import reload
from io import BytesIO, StringIO

import pytest
import yaml

from adr import query
from adr.cli import run_recipe

if sys.version_info > (3, 0):
    IO = StringIO
else:
    IO = BytesIO


class new_run_query(object):
    def __init__(self, test):
        self.test = test

    def __call__(self, query, *args, **kwargs):
        if query not in self.test['queries']:
            pytest.fail("no test data found for query '{}' in '{}.test'".format(
                        query, self.test['recipe']))
        for result in self.test['queries'][query]:
            yield result


def test_recipe(monkeypatch, recipe_test):
    monkeypatch.setattr(query, 'run_query', new_run_query(recipe_test))

    module = 'adr.recipes.{}'.format(recipe_test['recipe'])
    if module in sys.modules:
        reload(sys.modules[module])


    result = json.loads(run_recipe(recipe_test['recipe'], recipe_test['args'], fmt='json'))

    buf = IO()
    yaml.dump(result, buf)
    print("Yaml formatted result for copy/paste:")
    print(buf.getvalue())

    buf = IO()
    yaml.dump(recipe_test['expected'], buf)
    print("\nYaml formatted expected:")
    print(buf.getvalue())
    assert result == recipe_test['expected']
