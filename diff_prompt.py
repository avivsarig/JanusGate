import subprocess


def diff_to_str() -> str:
    diff_str = subprocess.run(
        ["git", "diff", "--staged"], capture_output=True, text=True
    ).stdout.strip()

    return diff_str
