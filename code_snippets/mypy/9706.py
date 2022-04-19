#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: fenc=utf-8:et:ts=4:sts=4:sw=4:fdm=marker
from typing import Optional, Sequence, Mapping
import collections

class ModuleInfo:
    def __init__(
        self,
        name: str,
        version_attributes: Sequence[str],
        min_version: Optional[str] = None
    ):
        self.name = name
        self._version_attributes = version_attributes
        self.min_version = min_version

MODULE_INFO: Mapping[str, ModuleInfo] = collections.OrderedDict([
    (name, ModuleInfo(name, *args))
    for (name, *args) in
    [
        ('sip', ['SIP_VERSION_STR']),
        ('colorama', ['VERSION', '__version__']),
        ('pypeg2', ['__version__']),
        ('jinja2', ['__version__']),
        ('pygments', ['__version__']),
        ('yaml', ['__version__']),
        ('adblock', ['__version__'], "0.3.2"),
        ('cssutils', ['__version__']),
        ('attr', ['__version__']),
        ('PyQt5.QtWebEngineWidgets', []),
        ('PyQt5.QtWebEngine', ['PYQT_WEBENGINE_VERSION_STR']),
        ('PyQt5.QtWebKitWidgets', []),
    ]
])
