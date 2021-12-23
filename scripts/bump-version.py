import subprocess
import sys
from enum import Enum


class UpgradeType(Enum):
    NONE = 'none'
    PATCH = 'patch'
    MINOR = 'minor'
    MAJOR = 'major'


MAJOR_KEYWORDS = ["breaking", "major"]
MINOR_KEYWORDS = ["feat", "feature", "minor"]
SKIP_BUMP_KEYWORDS = ["chore"]

upgrade_type = UpgradeType.NONE


def handle_subprocess_error(subprocess_result, error_message):
    if subprocess_result.returncode != 0:
        print(error_message)
        print(f"Return code {subprocess_result.returncode}")
        print("STDERR:")
        print(str(subprocess_result.stderr, "UTF-8"))
        print("STDOUT:")
        print(str(subprocess_result.stdout, "UTF-8"))
        exit(1)


if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    chart_name = sys.argv[1]
    print(f"Bumping version for: {chart_name}")
    print((subprocess.run(["pwd"], capture_output=True).stdout, "UTF-8"))
    get_commits_process = subprocess.run(["/bin/bash", "-c",
                                          f"git log --pretty=format:%s $(git tag --list --sort=-version:refname '{chart_name}-*' | head -n 1)..HEAD ."],
                                         cwd=f"../charts/{chart_name}", capture_output=True)

    handle_subprocess_error(get_commits_process, "Obtaining the commits since the last tag was not successful.")

    # get the needed upgrade type
    for line in str(get_commits_process.stdout, "UTF-8").split("/n"):
        if any(x.lower() in line.lower() for x in MAJOR_KEYWORDS):
            upgrade_type = UpgradeType.MAJOR
            break
        elif any(x.lower() in line.lower() for x in MINOR_KEYWORDS):
            upgrade_type = UpgradeType.MINOR
        elif upgrade_type != UpgradeType.MINOR and not any(x.lower() in line.lower() for x in SKIP_BUMP_KEYWORDS):
            upgrade_type = UpgradeType.PATCH

    if upgrade_type == UpgradeType.NONE:
        print("::set-output name=publish::false")
        exit(0)

    print(upgrade_type)
    subprocess_run = subprocess.run(f"bump2version {upgrade_type.value}", shell=True,
                                    cwd=f"../charts/{chart_name}",
                                    capture_output=True)
    handle_subprocess_error(subprocess_run, "Could not execute version bump")

    print("::set-output name=publish::false")
