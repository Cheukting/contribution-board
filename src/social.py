import requests
import os
from datetime import datetime, timezone, timedelta

now = datetime.fromisoformat("2024-07-21 09:05:34+00:00") #datetime.now(timezone.utc)
TOKENS = {"twitter": None,
"mastodon": os.environ["MASTODON_TOKEN"],
"linkein": None,}

def authenticate(accounts):
    for key, value in accounts.items():
        match key:
            case "twitter":
                pass
            case "mastodon":
                pass
            case "linkein":
                pass

def gen_txt(type, repo, link):
    if type == "new":
        return f"I have made a new contribution to #{repo}! See it at {link}"
    elif type == "merged":
        return f"My contribution at #{repo} have been accepted! See it at {link}"

def post_to_twitter(text, handle):
    pass

def post_to_mastodon(text, handle):
    domain = handle.split("@")[-1]
    headers = {"Authorization": TOKENS["mastodon"],
    "Content-Type": "application/json"}
    res = requests.post(
        f'https://{domain}/api/v1/statuses',
        headers=headers,
        json={"status": text}
    )

def post_to_linkedin(text, handle):
    pass

def post_to_each_social(pr, accounts, type):
    repo = pr["repository_url"].split('/')[-1]
    link = pr["url"]
    for key, value in accounts.items():
        match key:
            case "twitter":
                pass
            case "mastodon":
                post_to_mastodon(gen_txt(type, repo, link), accounts["mastodon"])
            case "linkein":
                pass


def post_to_social(prs, accounts):
    authenticate(accounts)
    for pr in prs:
        if pr["state"] == "open":
            created = datetime.fromisoformat(pr["created_at"])
            if now - created < timedelta(days=1):
                post_to_each_social(pr, accounts, "new")
        elif pr["state"] == "closed" and pr["pull_request"]["merged_at"] is not None:
            merged = datetime.fromisoformat(pr["pull_request"]["merged_at"])
            if now - merged < timedelta(days=1):
                post_to_each_social(pr, accounts, "merged")
