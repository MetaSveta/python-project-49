# Brain Games

[![Actions Status](https://github.com/MetaSveta/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MetaSveta/python-project-49/actions)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=MetaSveta_python-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=MetaSveta_python-project-49)

**Brain Games** is a collection of five console games built on the principle of brain training. Each game asks a series of questions, and the player needs to give the correct answer. If they answer all questions correctly, they win.

## Games

**Even Number Check** – determine if a number is even

**Calculator** – perform random arithmetic operations

**Greatest Common Divisor** – find the GCD of two numbers

**Arithmetic Progression** – guess the missing number in a progression

**Prime Number Check** – determine if a number is prime

---

## Requirements

This project was built using these tools:

| Tool                                                                   | Description                                             |
|------------------------------------------------------------------------|---------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                       | "An extremely fast Python package and project manager, written in Rust" |
| [Pytest](https://pytest.org)                                           | "A mature full-featured Python testing tool"            |
| [ruff](https://docs.astral.sh/ruff/)                                   | "An extremely fast Python linter and code formatter, written in Rust" |

---

## Setup

```bash
git clone https://github.com/MetaSveta/python-project-49.git
cd python-project-49
make install
make build
make package-install
```

## How to run

After installation, you can start any game directly from the terminal:

**Even Number Check**
```bash
make brain-even
```

**Calculator**
```bash
make brain-calc
```

**Greatest Common Divisor**
```bash
make brain-gcd
```

**Arithmetic Progression**
```bash
make brain-progression
```

**Prime Number Check**
```bash
make brain-prime
```

## Demonstrations
**Even Number Check**

[![asciicast](https://asciinema.org/a/qs8E4ABu0zSP9RGghPwhuL7GP.svg)](https://asciinema.org/a/qs8E4ABu0zSP9RGghPwhuL7GP)

**Calculator**

[![asciicast](https://asciinema.org/a/yNvRz02EV9nIdcZX1v346qmpC.svg)](https://asciinema.org/a/yNvRz02EV9nIdcZX1v346qmpC)

**Greatest Common Divisor**

[![asciicast](https://asciinema.org/a/xeTY4ayy3YNz3Xeu8KOVx2PtP.svg)](https://asciinema.org/a/xeTY4ayy3YNz3Xeu8KOVx2PtP)

**Arithmetic Progression**

[![asciicast](https://asciinema.org/a/1NsRbL1zNiWGUZZgNmrwOax09.svg)](https://asciinema.org/a/1NsRbL1zNiWGUZZgNmrwOax09)

**Prime Number Check**

[![asciicast](https://asciinema.org/a/bKi2JJZMAyIrTuAxAS5aSjvOA.svg)](https://asciinema.org/a/bKi2JJZMAyIrTuAxAS5aSjvOA)
