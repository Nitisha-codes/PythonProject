# 🔀 Day 5 — AND, OR, and the Curious Case of NOT

Kept today light on purpose — went hard yesterday, so today was about learning one topic well and then actually giving myself permission to rest.

## 🎯 What I learned
**Logical operators**: `and`, `or`, and `not`.

`and` and `or` made sense right away. `not` took a moment to click.

## 🧠 A concept that clicked (after some confusion)
I originally assumed `not` worked like flipping a comparison — like turning `==` into `!=`. But that's not what it does. It doesn't touch the *condition itself*, it flips the **resulting boolean value** — True becomes False, and False becomes True, after the condition has already been evaluated.

It actually reminded me of a chapter from Class 11 math here in Nepal — something in algebra involving conjunction, disjunction, and similar logic concepts. I don't remember the exact chapter name, but there was a version of "NOT" there too, where it just flipped true to false. Seeing basically the same logic show up in programming, just applied to code instead of a math proof, was a nice "oh, this connects" moment.

## 💪 Applying it — the exercise
Built a program that converts marks (0–100) into Nepal's grading system:
- Takes a mark as input
- Uses logical operators to sort it into the correct grade (A+, A, B+, B, C+, C, or NG/fail)
- Displays a message depending on the result — something encouraging for an A+ ("Congratulations on your outstanding performance!") and something gentler for a fail ("Better luck next time")

Nice, practical way to use logical operators instead of just testing them in isolation.

## 💻 Files in this folder
- `logical_opr.py` — practice with `and`, `or`, `not`, including the grading system exercise

## 📌 Tomorrow
Planning to move into conditional expressions next, building on today's logic.

---
🔐 *Day 5 of documenting my path into cybersecurity — short session today, but a solid one.*