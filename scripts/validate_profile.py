from pathlib import Path
import re, sys
root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text(encoding="utf-8")
refs = re.findall(r"\]\((\./assets/[^)]+)\)|src=\"(\./assets/[^\"]+)\"", readme)
paths = [a or b for a,b in refs]
missing = [p for p in paths if not (root / p[2:]).is_file()]
if missing:
    print("Missing README assets:", *missing, sep="\n- ")
    sys.exit(1)
print(f"OK: {len(paths)} local README asset references resolved.")
