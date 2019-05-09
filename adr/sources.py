import os
from itertools import chain
from pathlib import Path

from adr import config


class Source:
    def __init__(self, path):
        self.recipe_dir = Path(path).expanduser().resolve()
        self._recipes = None
        self._queries = None

    @property
    def query_dir(self):
        return self.recipe_dir / 'queries'

    @property
    def recipes(self):
        if self._recipes:
            return self._recipes

        self._recipes = [item.stem for item in self.recipe_dir.iterdir()
                         if item.is_file() and item.stem != '__init__' and item.suffix == '.py']
        return self._recipes

    @property
    def queries(self):
        if self._queries:
            return self._queries

        self._queries = [item.stem for item in self.query_dir.iterdir()
                         if item.is_file() if item.suffix == '.query']
        return self._queries


class SourceHandler:

    def __init__(self, sources):
        self._sources = []
        for source in set(sources):
            source = Path(source).expanduser().resolve()

            recipe_dirs = [p for p in source.glob('*recipes') if p.is_dir()]

            if not recipe_dirs:
                if source.as_posix() != os.getcwd():
                    print(f"warning: {source} does not contain any recipes!")
                continue

            for recipe_dir in recipe_dirs:
                source = Source(recipe_dir)
                if not source.recipes:
                    continue
                self._sources.append(source)

    def __len__(self):
        return len(self._sources)

    def __getitem__(self, i):
        return self._sources[i]

    @property
    def recipes(self):
        return chain(*[s.recipes for s in self._sources])

    @property
    def queries(self):
        return chain(*[s.queries for s in self._sources])

    def get(self, name, mode='recipe'):
        attr = 'queries' if mode == 'query' else 'recipes'
        suffix = '.query' if mode == 'query' else '.py'

        for s in self._sources:
            if name in getattr(s, attr):
                return getattr(s, f'{mode}_dir') / (name + f'{suffix}')


sources = SourceHandler(config.sources)
