# Codewars Solutions


![Solved](https://img.shields.io/badge/solved-0-brightgreen)
![8_kyu](https://img.shields.io/badge/8_kyu-0-informational)
![7_kyu](https://img.shields.io/badge/7_kyu-0-informational)
![6_kyu](https://img.shields.io/badge/6_kyu-0-informational)
![5_kyu](https://img.shields.io/badge/5_kyu-0-informational)
![4_kyu](https://img.shields.io/badge/4_kyu-0-informational)
![3_kyu](https://img.shields.io/badge/3_kyu-0-informational)
![2_kyu](https://img.shields.io/badge/2_kyu-0-informational)
![1_kyu](https://img.shields.io/badge/1_kyu-0-informational)


![Python](https://img.shields.io/badge/Python-0-blue)
![JavaScript](https://img.shields.io/badge/JavaScript-0-yellow)
![Java](https://img.shields.io/badge/Java-0-red)


[![Codewars Badge](https://www.codewars.com/users/<YOUR_USERNAME>/badges/large)](https://www.codewars.com/users/<YOUR_USERNAME>)


A curated collection of my Codewars kata solutions, organized by **difficulty** and **language**.
Each solution uses a consistent filename, and may include notes with complexity and alternative approaches.


---


## Structure
8-kyu/ python/ 8kyu_sum_of_positive__python__cw12345.py javascript/ 
8kyu_sum_of_positive__javascript__cw12345.js ...

- **Folder = Difficulty**
- **Subfolder = Language**
- **Filename = `{kyu}{underscore}{slug}__{language}__{kataId}.{ext}`**


---


## How I solve
1. Solve the kata on Codewars.
2. Mirror the solution here with a short note file (`.md`) if the kata is non-trivial.
3. Keep naming and folder structure consistent.
4. Automation updates the stats in this README on each push.


---


## Notes template (for `.md` files)


```md
# {Title} ({kyu}, {language})


**Kata:** https://www.codewars.com/kata/{kataId}
**Category/Tags:** strings, arrays, algorithms
**Time Complexity:** O(n)
**Space Complexity:** O(1)


## Approach
- Short explanation…


## Alternatives / Improvements
- Option B with tradeoffs…


## Tests
- Example inputs/outputs…

## Weekly Log
Week (ISO)	New Solved	Total	Notes
2025-W37	0	0	start

Roadmap / Goals

---


## .gitignore
```gitignore
# editors
.vscode/
.idea/


# Python
__pycache__/
*.pyc


# Node/JS
node_modules/


# OS
.DS_Store
Thumbs.db
