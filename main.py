import requests
import yaml
import json
import os

from svg_gen import gen_full, gen_compact
from validation import input_val

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

input_val(config)

headers = {
    "Authorization": os.environ["TOKEN"]
}

all_prs = []

for repo in config["repos"]:
    if config["state"] in ["open", "closed"]:
        res = requests.get(
            f'https://api.github.com/search/issues?q=repo:{repo}+type:pr+author:{config['username']}+state:{config['state']}',
            headers=headers,
        )
    else:
        res = requests.get(
            f'https://api.github.com/search/issues?q=repo:{repo}+type:pr+author:{config['username']}',
            headers=headers,
        )
    res_context = json.loads(res.text)
    all_prs += res_context["items"]

with open("output.json", "w") as file:
    json.dump(all_prs, file)

colors = {
    "size": config["size"],
    "bg": config["bg_color"],
    "bg_r": config["bg_r"],
    "pri": config["pri_color"],
    "sec": config["sec_color"],
}

with open(config["output"], "w") as file:
    if config["style"] == "compact":
        file.write(
            gen_compact(all_prs, headers, config["username"], config["state"], colors)
        )
    else:
        file.write(gen_full(all_prs, headers, colors))
