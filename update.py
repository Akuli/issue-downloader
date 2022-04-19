import ast
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


def find_and_save_snippets(repo, issue_num, description):
    filename = "code_snippets/" + repo.split("/")[-1] + "_" + str(issue_num) + ".py"

    python_codes = []

    # Find everything between two ```
    for potential_code in description.split("```")[1::2]:
        # First line is the "python3" of ```python3
        potential_code = potential_code.split('\n', 1)[-1]
        try:
            ast.parse(potential_code)
        except SyntaxError:
            pass
        else:
            python_codes.append(potential_code)

    if python_codes:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(python_codes))
        print(f"    Wrote {filename}")
    else:
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass
        else:
            print(f"    Deleted {filename}")


for repo in ["python/mypy", "python/typeshed", "python/typing"]:
    page = 1
    while True:
        print(f"{repo}: Requesting page {page}...")
        params = {
            "per_page": 100,
            "page": page,
            "state": "open",  # "open" is rate limit friendly, "all" is better
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
                find_and_save_snippets(repo, issue["number"], description)

        page += 1

    last_updated[repo] = time_at_start_of_script.isoformat()


with open("last_updated_utc.json", "w") as file:
    json.dump(last_updated, file)
