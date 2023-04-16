import sys
import subprocess

L = ["pathlib",
    "openpyxl",
    "pillow",
    "numpy"]

for i in range(0, 4):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
    L[i]])