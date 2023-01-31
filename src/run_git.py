def configure_safe_directory(directory: str) -> None:
    """
    Configure git safe.directory.
    """
    with gha_utils.group("Configure Git Safe Directory"):
        run_subprocess_command(
            ["git", "config", "--global", "--add", "safe.directory", directory]
        )
        
def run_subprocess_command(command: list[str]) -> None:
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        gha_utils.error(result.stderr)
        raise SystemExit(result.returncode)

    gha_utils.echo(result.stdout)

def git_diff() -> str:
    """Return the git diff"""
    return subprocess.run(["git", "diff"], capture_output=True, text=True).stdout    
