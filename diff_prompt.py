import subprocess


def diff_to_str(path: str) -> str:
    git_res = subprocess.run(
        ["git", "diff", "HEAD^", "HEAD", path], capture_output=True, text=True
    ).stdout.strip()
    return git_res
