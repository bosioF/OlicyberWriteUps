"""import zipfile
import os

counter1 = 3000

first_zip_file_path = '/home/bosio/Downloads/flag3000.zip'
extraction_path = f'/home/bosio/Downloads/flag{counter1}'

counter = 0

while counter < 3001:
    if counter == 0:
        with zipfile.ZipFile(first_zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)
    else:
        with zipfile.ZipFile(f'/home/bosio/Downloads/flag3000/flag{counter1- 1}.zip', 'r') as zip_ref:
            zip_ref.extractall(extraction_path)
    counter += 1
"""

import subprocess

contatore = 3000
directory = "/home/bosio/Downloads/flag3000"

while contatore > 0:
    zip_file = f"flag{contatore}.zip"
    try:

        result = subprocess.run(
            ["unzip", zip_file],
            capture_output=True,
            text=True,
            cwd=directory
        )

        print(f"Unzipping {zip_file}:")
        print(result.stdout)

        if result.stderr:
            print(f"Errori per {zip_file}:")
            print(result.stderr)

    except Exception as e:
        print(f"Errore durante l'estrazione di {zip_file}: {e}")

    contatore -= 1

