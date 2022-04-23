x = ((1, 'a', 1.4),)

for _, _, y in x:
    print(y)

import pkgutil

from somemod import _plugins

# trigger an import of all of the plugins
# https://github.com/python/mypy/issues/1422
plugins_path: str = _plugins.__path__  # type: ignore
mod_infos = pkgutil.walk_packages(plugins_path, f'{_plugins.__name__}.')
for _, name, _ in mod_infos:
    __import__(name, fromlist=['_trash'])
