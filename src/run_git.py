import subprocess

import github_action_utils as gha_utils  # type: ignore





def configure_safe_directory(directory: str) -> None:
    """
    Configure git safe.directory.
    """
    with gha_utils.group("Configure Git Safe Directory"):
        run_subprocess_command(
            ["git", "config", "--global", "--add", "safe.directory", directory]
        )




def git_commit_changes(
    commit_message: str,
    commit_author: str,
    commit_branch_name: str,
    force_push: bool = False,
) -> None:
    """
    Commit the changed files.
    """
    with gha_utils.group("Commit Changes"):
        run_subprocess_command(["git", "add", "."])
        run_subprocess_command(
            ["git", "commit", f"--author={commit_author}", "-m", commit_message]
        )
        push_command = ["git", "push", "-u"]

        if force_push:
            push_command.append("-f")

        push_command.extend(["origin", commit_branch_name])
        run_subprocess_command(push_command)


def git_has_changes() -> bool:
    """
    Check if there are changes to commit.
    """
    try:
        subprocess.check_output(["git", "diff", "--exit-code"])
        return False
    except subprocess.CalledProcessError:
        return True


def git_diff() -> str:
    """Return the git diff"""
    return subprocess.run(["git", "diff"], capture_output=True, text=True).stdout


def run_subprocess_command(command: list[str]) -> None:
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        gha_utils.error(result.stderr)
        raise SystemExit(result.returncode)

    gha_utils.echo(result.stdout)
