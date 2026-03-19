#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob

if [ "$#" -eq 0 ]; then
  echo "Uso: $0 file1 [file2 ...]"
  echo "Esempio: $0 *.txt"
  exit 1
fi

for f in "$@"; do
  if [ ! -f "$f" ]; then
    echo "Skipping (not a file): $f"
    continue
  fi

  name=$(basename -- "$f")
  base="${name%.*}"        # nome senza estensione
  dir="$base"
  i=1
  # evita collisioni: se esiste, crea base_1, base_2, ...
  while [ -e "$dir" ]; do
    dir="${base}_$i"
    i=$((i+1))
  done

  mkdir -p -- "$dir"
  # muove il file dentro la cartella e lo rinomina solve.py
  mv -- "$f" "$dir/solve.py"
  echo "Moved '$f' -> '${dir}/solve.py'"
done
