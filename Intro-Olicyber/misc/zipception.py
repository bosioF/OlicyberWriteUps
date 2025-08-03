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

