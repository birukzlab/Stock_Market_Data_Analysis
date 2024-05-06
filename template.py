import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Stock_Market_Data_Analysis"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"data/raw",
    f"data/processed",
    f"notebooks/EDA.ipynb",
    f"notebooks/data_collection.ipynb",
    f"notebooks/modeling.ipynb",
    f"src/__init__.py",
    f"src/data_collection.py",
    f"src/visualization.py",
    f"src/models.py",
    f"src/data_cleaning.py",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")