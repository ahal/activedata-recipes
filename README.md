[![Build Status](https://travis-ci.org/mozilla/active-data-recipes.svg?branch=master)](https://travis-ci.org/mozilla/active-data-recipes)
[![PyPI version](https://badge.fury.io/py/active-data-recipes.svg)](https://badge.fury.io/py/active-data-recipes)
[![PyPI version](https://readthedocs.org/projects/active-data-recipes/badge/?version=latest)](https://active-data-recipes.readthedocs.io)

# active-data-recipes

A repository of various ActiveData recipes. A recipe is a small snippet that runs one or more active
data queries and returns the output. Queries can sometimes be modified by command line arguments and
output can sometimes be post-processed.

Each recipe should try to answer a single question.

# Installation

    pip install active-data-recipes

or

    git clone https://github.com/mozilla/active-data-recipes
    cd active-data-recipes
    python setup.py develop

# Usage

Run:

    adr <recipe> <options>

For a list of recipes:

    adr --list

For recipe specific options see:

    adr <recipe> -- --help

# Recipes

See the [recipe documentation][1] for more information on which recipes are available and how to run
them.


[0]: https://github.com/klahnakoski/ActiveData/blob/dev/docs/jx_time.md
[1]: https://active-data-recipes.readthedocs.io/en/latest/recipes.html
