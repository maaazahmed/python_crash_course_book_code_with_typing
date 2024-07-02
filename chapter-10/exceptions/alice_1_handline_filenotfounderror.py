from pathlib import Path

path = Path("alic.txt")

try:
    content = path.read_text(encoding="utf-8")
except:
    print(f"Sorry, the file {path} does not exist.")