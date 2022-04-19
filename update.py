import ast
import glob
import json
import os
from datetime import datetime

import requests

try:
    os.mkdir("code_snippets")
except FileExistsError:
    pass

time_at_start_of_script = datetime.utcnow()
print("Updating code snippets starts at", time_at_start_of_script.isoformat())

try:
    with open("last_updated_utc.json", "r") as file:
        last_updated = json.load(file)
except FileNotFoundError:
    last_updated = {}


def delete_snippets(repo, issue_num):
    prefix = "code_snippets/" + repo.split("/")[-1] + "_" + str(issue_num)
    files = glob.glob(prefix + "_*.py")
    if os.path.isfile(prefix + ".py"):
        files.append(prefix + ".py")
    for file in files:
        print("    Deleting", file)
        os.remove(file)


def find_and_save_snippets(repo, issue_num, description):
    prefix = "code_snippets/" + repo.split("/")[-1] + "_" + str(issue_num)
    python_codes = []

    # Find everything between two ```
    for potential_code in description.split("```")[1::2]:
        # First line is the "py3" of ```py3
        potential_code = potential_code.split('\n', 1)[-1]
        try:
            ast.parse(potential_code)
        except SyntaxError:
            pass
        else:
            python_codes.append(potential_code)

    if len(python_codes) == 1:
        with open(prefix + ".py", "w", encoding="utf-8") as file:
            file.write(python_codes[0])
    else:
        for index, code in enumerate(python_codes):
            with open(f"{prefix}_{index}.py", "w", encoding="utf-8") as file:
                file.write(code)


for repo in ["python/mypy"]:
    page = 1
    while True:
        print(f"{repo}: Requesting page {page}...")
        params = {
            "per_page": 100,
            "page": page,
            "state": "open",  # TODO: change to "all" after initial download
        }
        if repo in last_updated:
            params["since"] = last_updated[repo] + "Z"

        response = requests.get(
            f"https://api.github.com/repos/{repo}/issues",
            params=params,
            headers={"accept": "application/vnd.github.v3+json"},
        )
        response.raise_for_status()

        updated_issues = response.json()
        if not updated_issues:
            break
        for issue in updated_issues:
            if "pull_request" not in issue:
                # it's actually an issue, github includes PRs in results
                print(f"  #{issue['number']}: {issue['title']}")
                description = issue["body"].replace("\r\n", "\n")
                delete_snippets(repo, issue["number"])
                find_and_save_snippets(repo, issue["number"], description)

        page += 1

    last_updated[repo] = time_at_start_of_script.isoformat()


with open("last_updated_utc.json", "w") as file:
    json.dump(last_updated, file)
