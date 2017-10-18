# active-data-recipes

A repository of various ActiveData recipes. A recipe is a small snippet that runs one or more active
data queries and returns the output. Queries can sometimes be modified by command line arguments and
output can sometimes be post-processed.

Each recipe should try to answer a single question.

# Installation

    pip install active-data-recipes

or

    git clone https://github.com/ahal/active-data-recipes
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

## Code Coverage

    adr code_coverage --path <path> --rev <rev>

Get code coverage information for the given `path` at `rev`. Both arguments are required.

## Hours on Try

    adr hours_on_try

Returns the total number of compute hours spent on try over the past week. The date range can be
modified with `--from` and `--to` using the format described [here][0]. For example:

    adr hours_on_try --from today-2month --to today-month

## Inspect

    adr inspect

Get information on the ActiveData schema. The above command returns the available tables. To see
the columns in a table, run:

    adr inspect --table task

## Task Durations

    adr task_durations

Get information on the longest running tasks. Returns the total count, average runtime and total
runtime over a given date range and set of branches.

## Try Usage

    adr try_usage

Prints stats on what percentage of try pushes are being scheduled with various different mechanisms
over the last week. The date range can be modified the same as the `hours_on_try` recipe.

<script src="https://gist.github.com/ahal/c78b6e78d36a5e7df8905d7e294d7762.js"></script>

## Try Users

    adr try_users

Prints stats on how often individual users are pushing to try over the last week. The date range can
be modified the same as the `hours_on_try` recipe.


[0]: https://github.com/klahnakoski/ActiveData/blob/dev/docs/jx_time.md
