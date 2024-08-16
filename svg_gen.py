import requests
import json

def add_bg(colors):
    if colors["bg"] is not None:
        return f'<rect width="100%" height="100%" rx="{colors["bg_r"]}" ry="{colors["bg_r"]}" fill="{colors["bg"]}"/>'
    else:
        return ""

def gen_full(all_prs, headers, colors):
    repo_cache = {}
    svgtext = add_bg(colors)
    m = colors["size"]

    for i, pr in enumerate(all_prs):
        url = pr["repository_url"]
        if url not in repo_cache.keys():
            res = requests.get(url, headers=headers)
            res_context = json.loads(res.text)
            repo_cache.update({url: res_context})
        else:
            res_context = repo_cache[url]
        svgtext += f"""<a href="{res_context["html_url"]}" target="_blank">
        <image x="{10*m}" y="{(15+i*50)*m}" height="{25*m}" width="{25*m}" href="{res_context["owner"]["avatar_url"]}" />
        <text x="{45*m}" y="{(20+i*50)*m}" fill="{colors["sec"]}" font-size="{15*m}">{res_context["full_name"]}</text>
      </a>\n<a href="{pr["html_url"]}" target="_blank">
        <text x="{45*m}" y="{(40+i*50)*m}" fill="{colors["pri"]}" font-size="{18*m}">{pr["title"]}</text>
      </a>\n"""

    content = f"""<?xml version="1.0" encoding="UTF-8"?>
    <svg height="{(10+len(all_prs)*50)*m}" width="{500*m}" xmlns="http://www.w3.org/2000/svg">
    {svgtext}
    </svg>"""

    return content


def gen_compact(all_prs, headers, user, state, colors):
    repo_cache = {}
    svgtext = add_bg(colors)
    m = colors["size"]

    for i, pr in enumerate(all_prs):
        url = pr["repository_url"]
        if url not in repo_cache.keys():
            res = requests.get(url, headers=headers)
            res_context = json.loads(res.text)
            repo_cache.update({url: {"count": 1, "content": res_context}})

        else:
            repo_cache[url]["count"] += 1

    for i, url in enumerate(repo_cache):
        res_context = repo_cache[url]["content"]
        svgtext += f"""<a href="{res_context["html_url"]}" target="_blank">
        <image x="{(15+i*100)*m}" y="{15*m}" height="{25*m}" width="{25*m}" href="{res_context["owner"]["avatar_url"]}" /></a>
        <a href="{res_context["html_url"]}/pulls?q=author%3A{user}+{f"is%3A{state}" if state in ["open", "closed"] else ""}" target="_blank">
        <text x="{(45+i*100)*m}" y="{35*m}" fill="{colors["pri"]}" font-size="{20*m}">{repo_cache[url]["count"]} {"PR" if repo_cache[url]["count"] ==1 else "PRs"}</text>
      </a>\n"""

    content = f"""<?xml version="1.0" encoding="UTF-8"?>
    <svg height="{55*m}" width="{len(repo_cache)*100*m}" xmlns="http://www.w3.org/2000/svg">
    {svgtext}
    </svg>"""

    return content
