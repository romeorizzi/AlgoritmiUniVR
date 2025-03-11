#!/usr/bin/env python3

from sys import stdin, stdout, stderr
import os
import ruamel.yaml as yaml
import shutil

# Funzione per caricare il file YAML
def load_yaml(filename):
    if not os.path.exists(filename):
        print(f"Errore: il file `{filename}` non è stato trovato!", file=stderr)
        exit(1)
    
    try:
        with open(filename) as stream:
            return yaml.YAML(typ='safe', pure=True).load(stream)
    except yaml.YAMLError as exc:
        print(f"Errore nel parsing del YAML: {exc}", file=stderr)
        exit(1)

# Funzione per creare il README.md e i symlink
def create_readme_and_symlinks(topic, tbody):
    readme_text = f'# {tbody["readme_title"]}\n\n'
    target_folder = os.path.join("..", "argomenti", topic)
    
    # Crea la cartella di destinazione se non esiste
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for problem_dict in tbody["problems"]:
        pcodename = problem_dict["codename"]
        # Aggiungi link al README
        readme_text += f'- [{pcodename}](../../problemi/{pcodename})\n'
        
        # Rimuovi eventuali symlink o file esistenti
        symlink_path = os.path.join(target_folder, pcodename)
        if os.path.exists(symlink_path):
            os.remove(symlink_path)

        # Crea il symlink
        problem_path = os.path.join("..", "..", "problemi", pcodename)
        os.symlink(problem_path, symlink_path)

    # Scrivi il README.md
    readme_path = os.path.join(target_folder, "README.md")
    with open(readme_path, "w") as fout:
        fout.write(readme_text)

    print(f" + {topic} gestito con successo!")

# Funzione principale
def main():
    DATAYAML_FILENAME = os.path.join(".", "mappa.yaml")
    datayaml = load_yaml(DATAYAML_FILENAME)

    print("Ok: file mappa.yaml letto e parsato con successo.")

    # Elaborazione di ciascun topic
    for topic_dict in datayaml:
        for topic, tbody in topic_dict.items():
            print(f" - {topic} trovato nel file YAML")
            create_readme_and_symlinks(topic, tbody)

    print("Ok: i symlink per gli argomenti ai problemi sono stati creati (simulati anche tramite i file README.md).")

# Esegui il programma
if __name__ == "__main__":
    main()
