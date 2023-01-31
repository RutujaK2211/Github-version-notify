from functools import cache
import github_action_utils as gha_utils  # type: ignore
import requests
import json
from .run_git import git_diff

@cache
def get_request_headers(github_token: str | None = None) -> dict[str, str]:
    """Get headers for GitHub API request"""
    headers = {"Accept": "application/vnd.github.v3+json"}

    if github_token:
        headers.update({"authorization": f"Bearer {github_token}"})

    return headers

def add_git_diff_to_job_summary() -> None:
    """Add git diff to job summary"""
    markdown_diff = (
        "<details>"
        "<summary>Git Diff</summary>"
        f"\n\n```diff\n{git_diff()}```\n\n"
        "</details>"
    )
    gha_utils.append_job_summary(markdown_diff)
    return markdown_diff
    

def post_msg_to_slack() -> None:
    slack_msg =  {'text':'Hello'}   
    weburl = "https://hooks.slack.com/services/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"
    requests.post(weburl,data=json.dumps(slack_msg))
    
