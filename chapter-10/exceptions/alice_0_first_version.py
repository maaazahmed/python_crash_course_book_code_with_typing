# from pathlib import Path

# path = Path("alice.txt")
# contents = path.read_text(encoding='utf-8')
# print(contents)



from pathlib import Path


path = Path("alice.txt")

content = path.read_text(encoding="utf-8")
print(content)