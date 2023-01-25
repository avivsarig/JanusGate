import subprocess


def list_added_files():
    added_files = (
        subprocess.run(
            ["git", "diff", "--staged", "--name-only"],
            capture_output=True,
            text=True,
        )
        .stdout.strip()
        .split("\n")
    )
    return added_files


def list_modified_files():
    modified_files = (
        subprocess.run(
            ["git", "diff", "--name-only", "HEAD", "HEAD~1"],
            capture_output=True,
            text=True,
        )
        .stdout.strip()
        .split("\n")
    )
    return modified_files
