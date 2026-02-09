# 🐍 Python Mini-Projects Collection

A collection of simple Python scripts and games created to practice core programming concepts, API integration, and game logic.

## 📂 Projects Overview

### 1. Car Fuel & Trim Fetcher (`GetTrims.py`)
A utility tool that connects to the **CarQuery API**.
* **Functionality:** Search for a car by Make and Year, select a specific Model and Trim, and get the **Fuel Type** and **Mixed Consumption** (L/km).
* **Tech:** REST API requests, JSON parsing.

### 2. Multiplayer Guess Game (`guess.py`)
A competitive number guessing game (1-10).
* **Functionality:** Supports multiple players, tracks win percentages, and features a **"Sudden Death"** mode if there is a tie at the end.
* **Tech:** Loops, Randomization, Logic flow.

### 3. Console Slot Machine (`Slots.py`)
A text-based casino simulation.
* **Functionality:** Place bets, manage your balance, and spin the reels using visual emojis (🍒 🍇 🥭). Includes payout logic for matching 2 or 3 symbols.
* **Tech:** Input validation, Betting logic.

---

## ⚙️ Setup & Installation

You need **Python 3.x** installed. The only external library required is `requests` for the Car Fetcher tool.

Install it via terminal:

```bash
pip install requests
