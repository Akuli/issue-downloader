from __future__ import annotations

import os
from pathlib import Path


def _calc_usage(target_path: Path | os.DirEntry) -> None:
    with os.scandir(target_path) as scanner:
        for entry in scanner:
            if entry.is_dir():
                _calc_usage(target_path)
            else:
                print('f')


_calc_usage(Path('.'))
