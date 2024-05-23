# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:34:08 2024

@author: Chris
"""
import yaml
import re

def conda_to_requirements(yaml_file, txt_file):
    with open(yaml_file, 'r') as stream:
        try:
            env_data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return

    dependencies = env_data.get('dependencies', [])

    pip_dependencies = []
    conda_dependencies = []

    for dep in dependencies:
        if isinstance(dep, str):
            # Extract name and version only, ignore build info
            match = re.match(r'^([a-zA-Z0-9_\-]+)=([0-9\.]+).*$', dep)
            if match:
                package, version = match.groups()
                conda_dependencies.append(f"{package}=={version}")
            else:
                conda_dependencies.append(dep)
        elif isinstance(dep, dict) and 'pip' in dep:
            pip_dependencies.extend(dep['pip'])

    with open(txt_file, 'w') as file:
        for dep in conda_dependencies:
            file.write(dep + '\n')
        for dep in pip_dependencies:
            file.write(dep + '\n')

if __name__ == "__main__":
    conda_to_requirements('environment.yml', 'requirements.txt')