from collections import defaultdict

from typing import DefaultDict
from mypy_extensions import TypedDict

RepoPath = str
RepoStatus = TypedDict('RepoStatus', {
    'branch': str,
    'remote': str,
    'clean': bool,
    # ...
}, total=False)

State2 = defaultdict(RepoStatus)            # type: DefaultDict[RepoPath, RepoStatus]
State3 = defaultdict(dict)                  # type: DefaultDict[RepoPath, RepoStatus]
State4 = defaultdict(lambda: RepoStatus())  # type: DefaultDict[RepoPath, RepoStatus]
State5 = defaultdict(lambda: dict())        # type: DefaultDict[RepoPath, RepoStatus]
State6 = defaultdict(lambda: {})            # type: DefaultDict[RepoPath, RepoStatus]
