# Contributor Guide

## 📜 Code of Conduct

Please be respectful to other contributors. We welcome everyone regardless of experience level.

---

## 🚀 How to Start

1. **Fork the repository**
2. **Clone your fork:**

```bash
git clone https://github.com/dlopeddtorred/hacker-simulator.git
cd hacker-simulator
```
### Install dependencies:
```bash
bash
pip install colorama
```
### Create a branch:

```bash
git checkout -b feature/new-feature
```
### Make your changes

#### Commit:

```bash
git add .
git commit -m "Add new feature"
``` 
### Push:

```bash
git push origin feature/new-feature
```
### Open a Pull Request

## 🎯 Contribution Areas
### 1. Servers (Easy)
Add servers in SERVERS:
```bash
python
{
    "id": "SRV-XXX",
    "name": "Server Name",
    "difficulty": 1-20,
    "reward": 100-200000,
    "clue_es": "Spanish clue",
    "clue_en": "English clue",
    "password": "password",
    "desc_es": "Spanish description",
    "desc_en": "English description"
}
```
### 2. Mini-games (Medium)
Add in MiniGames class:
```bash
python
@staticmethod
def new_game(difficulty, lang="es"):
    # Game logic
    return True/False
```
### 3. Tools (Easy)
Add in shop():
```bash
python
{"name": "🔧 New Tool", "price": 100, "desc_es": "ES Description", "desc_en": "EN Description"}
```
### 4. Achievements (Easy)
Add in ACHIEVEMENTS:
```bash
python
"id": {
    "name_es": "🏆 Spanish Name",
    "name_en": "🏆 English Name",
    "desc_es": "Spanish description",
    "desc_en": "English description",
    "reward": 100
}
```
### 5. Translations (Easy)
Add new language in TEXT dictionary.

### 6. Documentation (Easy)
Improve README.md

Create guides in docs/

## 📝 Code Style
Follow PEP 8 for Python

Use comments in English

Descriptive names

Max 80 characters per line

## 🐛 Reporting Bugs
Create an issue with:

Bug description

Steps to reproduce

Expected behavior

Screenshot (if applicable)

## 💡 Suggesting Improvements
Create an issue with:

Improvement description

Benefit to the project

Example code (optional)

## 🏆 Recognition
All contributors will be listed in:

Contributors

README.md

Thanks for making Hacker Simulator 2077 better! 🚀