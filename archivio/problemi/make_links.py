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
            datayaml = yaml.YAML(typ='safe', pure=True).load(stream)
    except yaml.YAMLError as exc:
        print(f"Errore nel parsing del YAML: {exc}", file=stderr)
        exit(1)
    print("Ok: data.yaml file successfully read and parsed.")
    return datayaml

# Funzione per creare il README.md di un singolo argomento
# (il testo del file README.md creato viene anche ritornato al chiamante per altro utilizzo)
# (viene inoltre popolato il dizionario `problemi`)
def create_readme_and_symlinks(topic, tbody):
    readme_text = f'# {tbody["readme_title"]}\n\n'
    target_folder = os.path.join("..", "argomenti", topic)
    
    # Crea la cartella di destinazione se non esiste
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for problem_dict in tbody["problems"]:
        pcodename = problem_dict["codename"]
        if pcodename in problemi:
            problemi[pcodename].append(topic)
        else:
            problemi[pcodename] = [topic]
        
        # Aggiungi riferimento al problema nel README in creazione
        readme_text += f'- [{pcodename}](../../problemi/{pcodename})\n'
        
        # Crea/aggiorna il symlink
        symlink_path = os.path.join(target_folder, pcodename)
        problem_path = os.path.join("..", "..", "problemi", pcodename)
        if os.path.exists(symlink_path):
            os.remove(symlink_path)
        os.symlink(problem_path, symlink_path)

    # Scrivi il README.md
    readme_path = os.path.join(target_folder, "README.md")
    with open(readme_path, "w") as fout:
        fout.write(readme_text)

    return readme_text


if __name__ == "__main__":
    DATAYAML_FILENAME = os.path.join(".", "mappa.yaml")
    datayaml = load_yaml(DATAYAML_FILENAME)
    print("Ok: file mappa.yaml letto e parsato con successo.")

    problemi = {}

    # Elaborazione di ciascun singolo topic, ma anche summary
    summary = "# Elenco problemi raccolti per argomenti\n\nUno stesso problema può ricadere sotto più argomenti.\n"
    for topic_dict in datayaml:
        for topic, tbody in topic_dict.items():
            print(f" + Found in file YAML: {topic=}")
            summary += "\n#" + create_readme_and_symlinks(topic, tbody)
            print(f" = Successfully managed: {topic=}")
    with open(os.path.join(".", "README.md"), "w") as fout:
        fout.write(summary)

    print("\nOk 1: in ciascun argomento (ossia subfolder del folder `argomenti`) ho crato i symlink ai problemi di pertinenza ed il file README.md con la loro lista. Ho inoltre creato un README.md complessivo nella presente cartella (`problemi`).")
    
    for pcodename, lista_topics in problemi.items():
        if not os.path.exists(pcodename):
            print(f"Errore: folder di problema `{pcodename}` non trovato!", file=stderr)
        else:
            with open(os.path.join(".", pcodename, "README.md"), "w") as fout:
                fout.write("# Argomenti/tecniche di pertinenza\n\n - ")
                fout.write("\n - ".join(lista_topics) + "\n")
    
    print("\nOk 2: per ciascun problema ho listato gli argomenti che tocca.")
