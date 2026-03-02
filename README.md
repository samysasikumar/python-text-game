# 🐇 Lab Bunny 2.0

A text-based adventure game written in Python, where you play as a lab bunny escaping into the wild forest — and must survive what comes next.

---

## 🎮 How to Play

Make sure you have **Python 3** installed, then run:

```bash
python Lab_bunny_2_0.py
```

No extra libraries needed — runs with standard Python only.

---

## 📖 About the Game

You are a lab bunny who squeezes through the gates of a research facility and escapes into a dark, unknown forest. You name yourself, describe your fur, and make choices that determine your fate.

Every decision matters:
- Which path do you take at the fork?
- Do you hide from the fox — or run?
- Do you share what little you have with the wild rabbits who could shelter you?

The story branches based on your choices, and your inventory changes throughout the game depending on what you find, take, or lose.

---

## 🗺️ Game Structure

```
Intro → Character Setup → Chapter 1: The Fork
                              ├── Left  → Chapter 2A: The Stream → Chapter 3
                              └── Right → Chapter 2B: The Glow   → Chapter 3
                                                                       ├── Ending: Safe 🌙
                                                                       └── Ending: Onward 🌲
```

---

## 🧠 Concepts Used

This project was built to practice core Python concepts:

| Concept | Where it's used |
|--------|----------------|
| `print()` and `input()` | All story text and player prompts |
| f-strings | Personalizing story text with player's name, weight, fur color |
| `if / else` conditionals | Branching story paths based on player choices |
| `while` loops | Input validation — keeps asking until a valid choice is given |
| Lists | Inventory system — items added/removed based on choices |
| Functions | Each chapter is its own function for clean, organized code |
| `import time` | `time.sleep()` used for dramatic pauses between scenes |

---

## 💡 What I Learned

- How to structure a larger Python program using functions
- How to use conditionals to create branching narratives
- How to manage game state (inventory) across multiple scenes
- How to make input validation reusable with a helper function
- How to use f-strings to make the story feel personal and dynamic

---

## 📁 Files

| File | Description |
|------|-------------|
| `Lab_bunny_2_0.py` | Main game file — run this to play |
| `README.md` | This file |

---

## ✨ About

Built by **Samy Sasikumar** as part of the **UW Youth & Teens Program - Coding in Python Course**.  
High School Student · Redmond, WA

🐙 [github.com/samysasikumar](https://github.com/samysasikumar)

---

*Happy hopping. 🐇*
