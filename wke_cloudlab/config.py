'''
Utils to parse the wke-cloudlab.toml file
'''

import os
import tomllib

def get_defaults():
    ''' Load the default configuration options (if any) '''

    config_path = os.path.expanduser("~/.wke-cloudlab.toml")
    defaults = {}

    if os.path.exists(config_path):
        with open(config_path, 'rb') as file:
            config = tomllib.load(file)
            defaults_toml = config.get("defaults", {})

            found = []

            for key in ["hardware-type", "os-image", "username", "workdir"]:
                defaults[key] = defaults_toml.get(key, None)
                if defaults[key] is not None:
                    found.append(key)

            if len(found) == 0:
                print(f"{config_path} existed, but found no default values")
            else:
                print(f"Found default value(s) for {found} at {config_path}")

    return defaults
