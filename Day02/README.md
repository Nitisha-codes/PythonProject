# 🔁 Day 2 — Teaching Python to Understand Me

Today's topics: **type casting** and **user input**. Basically, teaching Python how to actually listen to what a human types in.

## 🎯 What I learned
- `input()` always returns a string — even if you type a number, Python sees it as text until you tell it otherwise
- How to convert between types using `int()`, `float()`, and `str()`
- Why skipping type casting leads to weird bugs (like trying to "add" two numbers and getting them stuck together instead)

## 🧠 A concept that clicked
I used to think computers were "smart" by default. Turns out, Python is very literal — if you don't explicitly say "treat this as a number," it just won't. Type casting is basically me telling Python "no really, I promise this is a number."

## 🐛 A moment I got stuck (the real plot twist of the day)
The Python part was fine — the chaos today was 100% **Git**. I accidentally pushed my `.venv` and `.idea` folders (auto-generated system folders that were never supposed to be tracked) straight to GitHub. Cue a full mini panic spiral, thinking two days of work had vanished.

Turns out: nothing was lost. Ever. Git had it all safely logged the whole time. I learned how to:
- Reset a branch back to a clean state
- Create a `.gitignore` file
- Untrack folders with `git rm -r --cached`

Lesson of the day: **panicking makes Git scarier than it actually is.** Stop, check what's actually there, then act.

## 💪 Applying it — mini exercises
Beyond just following along, I built two small programs to actually use what I learned:
- A **rectangle area calculator** — takes length and width as input, casts them properly, and calculates the area
- A **mini shopping cart program** — small and simple, but good practice for combining input, type casting, and basic logic

## 💻 Files in this folder
- `typecasting.py` — practice converting between data types
- `userinput.py` — practice taking and using user input
- `exercise.py` — the rectangle area calculator and shopping cart mini-programs
- `.gitignore` (repo-level) — now keeps `.venv` and `.idea` out of future commits

## 📌 Tomorrow
Moving on — hopefully with a calmer Git experience this time. 😅

---
🔐 *Day 2 of documenting my path into cybersecurity — turns out learning Git is its own subject entirely.*