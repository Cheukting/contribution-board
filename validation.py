ERR_RULES = {
    "username": "input is None",
    "repos": "input is None",
    "output": "input is None",
    "state": "input not in ['all', 'open', 'closed']",
    "style": "input not in ['full', 'compact']",
    "size": "float(input) <= 0",
    "bg_r": "int(input) <= 0",
    "pri_color": "input is None",
    "sec_color": "input is None",
}


def input_val(config):
    for key, rule in ERR_RULES.items():
        input = config[key]
        if eval(rule):
            raise ValueError(f"{key}: {rule}")
