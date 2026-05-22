# 🏗️ Low Level Design (LLD) — Learning in Public

A collection of projects I'm building while learning **Low Level Design** from scratch.

Each project is hands-on — I design the class diagram first, then write the code. No copy-paste. No tutorials. Just building and breaking things until it clicks.

> "Building > Reading"

---

## 👤 About Me

I'm **Dev**, a Semester 6 AI student at ADIT, CVM University, India.  
My background is in AI/backend (LangChain, FastAPI, LangGraph) — but I'm leveling up on system design and OOP fundamentals to become a well-rounded engineer.

---

## 📂 Projects

| # | Project | Concepts Covered | Status |
|---|---------|-----------------|--------|
| 01 | [Notification System](./01-notification-system/) | S, O, D — Single Responsibility, Open/Closed, Dependency Inversion | ✅ Done |
| 02 | Payment Processing System | L, I — Liskov Substitution, Interface Segregation | 🔨 Next |
| 03 | More coming... | | ⏳ |

---

## 🧠 SOLID Principles — Quick Reference

Before diving into projects, here's a one-line summary of each principle:

| Principle | What it means | Real-life analogy |
|-----------|--------------|-------------------|
| **S** — Single Responsibility | One class, one job | Cook cooks. Driver drives. |
| **O** — Open/Closed | Add features by adding code, not editing old code | Plug into the power strip, don't rewire it |
| **L** — Liskov Substitution | Child classes must fully honor what parent promised | A "vehicle" must actually transport |
| **I** — Interface Segregation | Don't force classes to implement things they don't need | Don't make the chef sign a plumbing contract |
| **D** — Dependency Inversion | Depend on abstractions, not concrete classes | Hire "licensed driver", not Rahul specifically |

---

## 📁 Repo Structure

```
lld-projects/
│
├── README.md                        ← you are here
│
├── 01-notification-system/
│   ├── notification_system.py
│   ├── README.md
│   └── assets/
│       └── class_diagram.png
│
├── 02-payment-system/
│   ├── payment_system.py
│   ├── README.md
│   └── assets/
│       └── class_diagram.png
│
└── ...
```

---

## 🔨 My Process (for every project)

1. **Understand the problem** — what are we building and why
2. **Identify the bad design** — what breaks without SOLID
3. **Draw the class diagram** — boxes, arrows, relationships on paper
4. **Write the code** — class by class, no skipping
5. **Test it** — does adding a new feature break anything?
6. **Document it** — README + LinkedIn post

---

## 🛠️ Tech

- **Language:** Python 3.11+
- **Concepts:** OOP, SOLID, Design Patterns (coming soon)
- **Tools:** Just a text editor and a pen for diagrams

No frameworks. No libraries. Pure Python — because LLD is about thinking, not tooling.

---

## 📬 Connect

If you're also learning LLD, let's connect.  
I post about what I'm building on [LinkedIn](https://www.linkedin.com/in/devdoshi19/).

---

*This repo grows one project at a time. Every commit is a step forward.*