# 🐰 Bunny Escape — A Text-Based Adventure Game

A Python text-based adventure game where you play as a lab bunny who has just escaped into a dark forest. Every choice you make changes what happens next.

---

## Storyline

You are a bunny who wriggles through a hole in cold metal gates and escapes into an unknown forest. You are carrying half a carrot, a number tag on a string, and a rock. Night is falling. You need to find shelter — but the forest is full of surprises, and the humans are looking for you.

---

## Features

- **Branching story** — every decision leads to a different path and outcome
- **Inventory system** — items you carry affect what choices are available
- **Character creation** — name, weight, and fur color all influence the story
- **Multiple endings** — survive the night, get caught, or meet a hungry fox
- **Input validation** — the game keeps asking until you give a valid answer

---

## How to Play

**Requirements:** Python 3.x

**Run the game:**
```bash
python main.py
```

The game runs entirely in the terminal. Answer each prompt by typing your response and pressing Enter. Yes/no questions only accept `yes` or `no`.

---

## Endings

There are **6 possible endings** depending on the choices you make. Can you find all the safe ones?

| Path | Outcome |
|------|---------|
| Hill → hide | Caught by lab worker |
| Hill → run | Caught in a net |
| Burrow → share carrot | Safe night with opossum family |
| Burrow → keep carrot | Safe night with opossum family |
| Cave → greet → brown fur | Safe night in the bear's cave |
| Cave → greet → not brown fur | Eaten by a fox |
| Cave → stay silent | Eaten by a fox |

---

## What I Learned

This project was built as part of the **UW Youth & Teen — Coding in Python I** program. Through building this game I practiced:

- Writing and calling functions (`def ask_yes_no`, `def ask_place`)
- Using `while` loops for game flow and input validation
- Working with lists and the `.remove()` method for inventory management
- `if / elif / else` branching for story logic
- f-strings for dynamic output
- Thinking about edge cases — what happens if a player types the wrong thing?

---

## Project Structure

```
python-text-game/
└── main.py      # Full game — story, logic, and all branching paths
```

---

## Author

**Samy Sasikumar** · High School Student · Redmond, WA
🐙 [github.com/samysasikumar](https://github.com/samysasikumar)

---

*Built with 🐇 · UW Youth & Teen — Coding in Python I · 2026*
