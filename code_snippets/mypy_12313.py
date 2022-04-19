import _editable_pkg_typed

from editables.redirector import RedirectingFinder as F
F.install()
F.map_module('editable_pkg_typed', '/path/to/package/editable_package_typed/__init__.py')

INSTALLER
LICENSE
METADATA
RECORD
REQUESTED
WHEEL

{
    "url": "file:///path/to/package",
    "dir_info": {
        "editable": true
    }
}

LICENSE
README.md

__init__.py
py.typed

