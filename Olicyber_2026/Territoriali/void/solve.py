import re
import subprocess

res = subprocess.run(
    ["ltrace", "-e", "putchar", "./void"],
    capture_output=True,
    text=True
)

flag_chrs = re.findall(r"putchar\((\d+)[^\d]", res.stderr)
print("".join(chr(int(c)) for c in flag_chrs))
