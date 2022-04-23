import ast
import json
from pathlib import Path
from datetime import datetime

import requests

time_at_start_of_script = datetime.utcnow()
print("Updating code snippets starts at", time_at_start_of_script.isoformat())

try:
    with open("last_updated_utc.json", "r") as file:
        last_updated = json.load(file)
except FileNotFoundError:
    last_updated = {}


def find_and_save_snippets(repo, issue_num, description):
    relative_path = repo.split("/")[-1]
    if repo == "python/mypy":
        # This repo has many issues....
        range_start = issue_num - (issue_num % 1000)
        relative_path += f"/{range_start}-{range_start+999}"

    file = Path("code_snippets") / relative_path / (str(issue_num) + ".py")
    file.parent.mkdir(parents=True, exist_ok=True)

    python_codes = []

    # Find everything between two ```
    for potential_code in description.split("```")[1::2]:
        # First line is the "python3" of ```python3
        potential_code = potential_code.split('\n', 1)[-1]
        if "[mypy]" not in potential_code:
            try:
                ast.parse(potential_code)
            except SyntaxError:
                pass
            else:
                python_codes.append(potential_code)

    if python_codes:
        file.write_text("\n".join(python_codes))
        print(f"    Wrote {file}")
    else:
        try:
            file.unlink()
        except FileNotFoundError:
            pass
        else:
            print(f"    Deleted {file}")


# please keep repo list in README up to date
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
