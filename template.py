import os
import pathlib
import logging

logging.basicConfig(level=logging.INFO, format = '[%(ascitime)s: %(message)s:]')

project_name = "transformer_text_summary"

list_of_files = [
    ".github/wordflows/.gitkeep" # Placeholder for the YAML file for CI/CD. To be replaced later.
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/trial_notebook.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = pathlib.Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info('Creaing empty file')
    else:
        logging.info(f"{filename} already exists")