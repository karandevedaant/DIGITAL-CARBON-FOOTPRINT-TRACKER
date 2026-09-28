"""
storage.py  (Module 2)
----------------------
Saves and loads the user's activity entries in a JSON file so the
data is still there the next time the program runs.

Each entry is a dictionary like:
{"date": "2026-09-28", "category": "transport", "item": "bus",
 "quantity": 10.0, "emission": 0.89}
"""

import json
import os
from datetime import date

DATA_FILE = os.path.join("data", "entries.json")


def load_entries():
    """Read all entries from the file. Returns an empty list if none."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # file is empty or damaged, start fresh instead of crashing
        print("Warning: could not read saved data. Starting with empty list.")
        return []


def save_entries(entries):
    """Write the full list of entries to the file."""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=2)


def add_entry(category, item, quantity, emission, entry_date=None):
    """Create a new entry, add it to the file and return it."""
    if entry_date is None:
        entry_date = date.today().isoformat()

    entry = {
        "date": entry_date,
        "category": category,
        "item": item,
        "quantity": quantity,
        "emission": emission,
    }
    entries = load_entries()
    entries.append(entry)
    save_entries(entries)
    return entry


def clear_entries():
    """Delete all saved data."""
    save_entries([])
