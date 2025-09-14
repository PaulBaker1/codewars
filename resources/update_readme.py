import re
import os
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DIFFS = ["8-kyu","7-kyu","6-kyu","5-kyu","4-kyu","3-kyu","2-kyu","1-kyu"]


# Map badge labels in README to counters we compute
LANG_BADGE_LABELS = ["Python","JavaScript","Java","TypeScript","Go","CSharp","Kotlin"]




def list_solutions():
counts_by_diff = Counter()
counts_by_lang = Counter()
total = 0


for d in DIFFS:
dpath = ROOT / d
if not dpath.is_dir():
continue
for lang_dir in dpath.iterdir():
if not lang_dir.is_dir():
continue
lang = lang_dir.name.lower()
for f in lang_dir.rglob("*.*"):
# ignore notes
if f.suffix.lower() == ".md":
continue
total += 1
counts_by_diff[d] += 1
counts_by_lang[lang] += 1
return total, counts_by_diff, counts_by_lang




def patch_badge(content: str, label: str, value: int) -> str:
# Replace first shield that matches label; keep color suffix intact
pattern = re.compile(rf"!\[.*?\]\(https://img\.shields\.io/badge/{re.escape(label)}-\d+-(.+?)\)")
return pattern.sub(lambda m: f"![{label}](https://img.shields.io/badge/{label}-{value}-{m.group(1)})", content, count=1)




def main():
total, by_diff, by_lang = list_solutions()
text = README.read_text(encoding="utf-8")


text = patch_badge(text, "solved", total)


for d in DIFFS:
key = d.replace("-", "_") # e.g. 8-kyu -> 8_kyu
text = patch_badge(text, key, by_diff[d])


for lang in LANG_BADGE_LABELS:
val = by_lang.get(lang.lower(), 0)
text = patch_badge(text, lang, val)


README.write_text(text, encoding="utf-8")
print(f"Updated README: total={total}, by_diff={dict(by_diff)}")




if __name__ == "__main__":
main()