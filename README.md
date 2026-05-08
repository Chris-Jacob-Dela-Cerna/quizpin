# QuizPin
**Version 1.0.0** · Python terminal quiz app

QuizPin is a terminal program that lets you create your own quiz items, store them persistently on your computer, and run them as either multiple choice or identification quizzes — all from the command line.

---

## Features

**Create quizzes**
- Enter a minimum of 4 items in `term - definition` format
- Items are saved as a named CSV file inside a local `quizzes` folder

**Run quizzes**
- Choose from your list of saved quizzes
- Select a mode: multiple choice or identification
- Number of questions matches the number of items you created (supports 100+ items)
- Multiple choice uses definitions as questions, with randomly selected terms as choices
- Identification requires an exact match to the term (case-insensitive)
- Score shown at the end, with an option to review correct answers

**Manage quizzes**
- View all saved quizzes
- Rename or delete any quiz file

---

## How to Run

1. Download or clone the `quizpin` folder
2. Navigate into the folder
3. Run the program:

```bash
python main.py
```

The program will greet you and walk you through a menu:

```
a - Create quiz items
b - Start a quiz
c - Manage quizzes
d - Exit
```

Press **Enter** at any pause to continue. This pacing is intentional.

---

## Running Tests

```bash
cd tests
pytest
```

---

## Built With

- **Python 3.14.3**
- `csv` — reading and writing quiz data
- `os` — file path handling
- `sys` — program exit handling
- `pytest` — unit testing (third-party)

---

## Planned Features (v2.0.0)

- **Custom question count** — choose how many questions to pull from your quiz instead of running all of them
- **Paginated quiz list** — currently lists all quizzes at once; next version will show 10 per page for large collections
- **Smarter multiple choice** — use `difflib` to pull in similar-but-wrong terms from outside the quiz list for harder distractors
- **Fuzzy identification matching** — allow close answers to count (e.g. "a red apple" matching "red apple"), reducing harsh penalization for minor typos
- **Answer comparison on review** — show your answer alongside the correct answer clearly when reviewing results

---

## Background

This is my first personal portfolio project, built out of passion and curiosity.

I started learning to code from scratch in March 27, 2026. QuizPin began as a Week 6 exercise inside my `cs50p-projects` repo but grew ambitious enough to outgrow even the master challenges I had been building there — so I gave it its own home.

It took 26+ hours across 10 days to finish, and I'm proud of it.