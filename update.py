import os
import json
from datetime import datetime

import requests

try:
    os.mkdir("code_snippets")
except FileExistsError:
    pass


with open("last_updated_utc.txt", "r") as file:
    old_last_updated = datetime.fromisoformat(file.read().strip())
new_last_updated = datetime.utcnow()


issues = []

page = 1
while True:
    print("Requesting page", page, "...")
    response = requests.get(
        "https://api.github.com/repos/python/mypy/issues",
        params={
            "per_page": 100,
            "page": page,
            "state": "all",
            "since": old_last_updated.isoformat() + "Z",
        },
        headers={
            "accept": "application/vnd.github.v3+json",
        },
    )
    response.raise_for_status()
    new_issues = response.json()
    if not new_issues:
        break
    for issue in new_issues:
        if "pull_request" not in issue:
            # it's actually an issue, github includes PRs in results
            print(f"  #{issue['number']}: {issue['title']}")
            print(repr(issue["body"]))
    page += 1

with open("last_updated_utc.txt", "w") as file:
    print(new_last_updated.isoformat(), file=file)
