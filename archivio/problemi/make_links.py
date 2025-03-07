#!/usr/bin/env python3

from sys import stdin, stdout, stderr
import os.path
import ruamel.yaml as yaml
import shutil
from pathlib import Path

read_yaml = yaml.YAML(typ='safe', pure=True)
write_yaml = yaml.YAML()
write_yaml.preserve_quotes = True


YAML_DIR = "."
DATAYAML_FILENAME = os.path.join(YAML_DIR,"mappa.yaml")
if not os.path.exists(DATAYAML_FILENAME):
    print(f"data.yaml file `{DATAYAML_FILENAME}` not found!")
    exit(1)
with open(DATAYAML_FILENAME) as stream:
    try:
        datayaml = read_yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc, file=stderr)
        exit(1)
print("Ok: data.yaml file successfully read and parsed.")

for topic_dict in datayaml:
  for topic, tbody in topic_dict.items():  
    print(f" - {topic=} has been encountered in the yaml file")
    readme_text = f'# {tbody["readme_title"]}\n\n'
    target_folder = os.path.join("..", "argomenti", topic)
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)
    for problem_dict in tbody["problems"]:
        pcodename = problem_dict["codename"]
        #print(f" - - {pcodename=}, {problem_dict=}")  
        readme_text += f'- [{pcodename}](../../problemi/{pcodename})\n'
        os.system(f'rm {os.path.join(target_folder, pcodename)}')
        os.system(f'ln -s -t {target_folder} ../../problemi/{pcodename}')
    fout = open(os.path.join(target_folder, "README.md"), "w")
    fout.write(readme_text)
    fout.close()
    print(f" + {topic=} has been successfully managed!")

print("Ok: the symlinks from the arguments to the problems have been created (also emulated via README.md files).")
