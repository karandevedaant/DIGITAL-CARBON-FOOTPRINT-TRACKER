# Digital Carbon Footprint Tracker

A simple command-line Python application that helps you record your daily
activities (travel, electricity, food, cooking gas, waste), calculates the
CO2 they produce, and gives you reports and tips to reduce your footprint.

**Author:** Vedaant Karande (B.Tech First Year)
**Language:** Python 3 (standard library only, no GUI)

---

## Features

- Add daily activities in 5 categories: transport, electricity, food, cooking gas, waste
- Automatic CO2 calculation using emission factors
- Today's summary compared with the average Indian per-person footprint
- Category-wise report (this month / all time) with a text bar chart
- Personalised tip based on your highest-emission category
- Data is saved in a JSON file, so it is remembered between runs
- Input validation (wrong inputs do not crash the program)

## Project Structure

```
carbon-footprint-tracker/
|-- main.py            # Menu / entry point (run this file)
|-- calculator.py      # Module 1: emission factors and CO2 calculation
|-- storage.py         # Module 2: saving and loading data (JSON file)
|-- analysis.py        # Module 3: totals, comparison, chart data, tips
|-- requirements.txt   # Dependency note (none needed)
|-- README.md          # This file
|-- .gitignore
|-- data/              # Created automatically when you save first entry
```

## Requirements

- Python 3.8 or newer
- A terminal (Command Prompt, PowerShell, Terminal, etc.)
- No internet connection or extra libraries needed while running

## Step-by-Step Setup and Run Instructions

### Step 1: Check that Python is installed

Open a terminal and type:

```
python --version
```

If it shows `Python 3.x.x` you are ready. On Mac/Linux you may need to use
`python3` instead of `python` in every command below. If Python is not
installed, download it from https://www.python.org/downloads/

### Step 2: Get the project

Using Git:

```
git clone https://github.com/<github-username>/<repo-name>.git
cd <repo-name>
```

(Or download the repository as a ZIP from GitHub, extract it, and open a
terminal inside the extracted folder.)

### Step 3: (Optional) Create a virtual environment

```
python -m venv venv
```

Activate it:

- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### Step 4: Install dependencies

This project uses only the Python standard library, so nothing has to be
installed. Running the command below is safe and simply confirms this:

```
pip install -r requirements.txt
```

### Step 5: Configuration

No configuration is needed. The program creates a `data/` folder and an
`entries.json` file automatically the first time you save an activity.
Run the program from inside the project folder so the data file is
created in the right place.

### Step 6: Run the project

```
python main.py
```

## How to Use

When the program starts you will see this menu:

```
1. Add an activity
2. Today's summary
3. Category report
4. View history
5. Get a tip to reduce footprint
6. Delete all data
7. Exit
```

Example: to log a 15 km motorbike ride, choose `1`, then category
`1` (transport), then activity `2` (motorbike), then type `15`.
The program prints the CO2 produced and saves it.

## Sample Output

```
--- Category Report: All time ---
transport        1.54 kg
electricity     98.40 kg  ##############################
food             3.60 kg  #

Total: 103.55 kg CO2
Trees needed to absorb this in a year: about 4.9
```

## How the Calculation Works

```
CO2 (kg) = amount of activity x emission factor
```

Example: 10 km by bus = 10 x 0.089 = 0.89 kg CO2.

The emission factors are approximate averages from public sources and are
used for awareness and learning. They are not for official carbon accounting.
You can change the values in the `EMISSION_FACTORS` dictionary in `calculator.py`.

## Troubleshooting

| Problem | Solution |
|---|---|
| `python` is not recognised | Use `python3`, or reinstall Python and tick "Add to PATH" |
| `ModuleNotFoundError` for calculator/storage/analysis | Run the command from inside the project folder |
| Saved data looks wrong | Choose option 6 in the menu, or delete the `data/` folder |

## Future Improvements

- Export reports to CSV
- Weekly graphs using matplotlib
- Set a monthly carbon budget with alerts
