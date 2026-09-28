"""
analysis.py  (Module 3)
-----------------------
Turns the saved entries into useful information: totals, category
breakdown, comparison with an average person, text bar chart and
personalised tips.
"""

# Approximate average daily footprint of one person in India
# (about 1.9 tonnes CO2 per year / 365 days = ~5.2 kg per day)
AVERAGE_DAILY_KG = 5.2

TIPS = {
    "transport": "Use bus, metro or train instead of a car or bike, "
                 "or cycle/walk for short trips. Share rides when possible.",
    "electricity": "Switch off fans and lights when leaving a room, use "
                   "LED bulbs and 5-star rated appliances.",
    "food": "Try having more vegetarian meals. Red meat has the highest "
            "footprint per meal.",
    "cooking_gas": "Use a pressure cooker and keep lids on pots to save LPG.",
    "waste": "Reduce, reuse and recycle. Compost kitchen waste and avoid "
             "single-use plastic.",
}


def total_emission(entries):
    """Sum of emission of all given entries."""
    total = 0.0
    for e in entries:
        total += e["emission"]
    return round(total, 3)


def filter_by_date(entries, day):
    """Return only the entries of one date (format YYYY-MM-DD)."""
    return [e for e in entries if e["date"] == day]


def filter_by_month(entries, month):
    """Return only the entries of one month (format YYYY-MM)."""
    return [e for e in entries if e["date"].startswith(month)]


def totals_by_category(entries):
    """Return a dictionary {category: total kg CO2}."""
    result = {}
    for e in entries:
        cat = e["category"]
        result[cat] = round(result.get(cat, 0) + e["emission"], 3)
    return result


def highest_category(entries):
    """Return the category with the biggest emission (or None)."""
    totals = totals_by_category(entries)
    if not totals:
        return None
    return max(totals, key=totals.get)


def compare_with_average(daily_total):
    """Return a message comparing one day's total with the average."""
    diff = round(daily_total - AVERAGE_DAILY_KG, 2)
    if diff > 0:
        return "That is %.2f kg ABOVE the average of %.1f kg/day." % (
            diff, AVERAGE_DAILY_KG)
    if diff < 0:
        return "Great! That is %.2f kg BELOW the average of %.1f kg/day." % (
            abs(diff), AVERAGE_DAILY_KG)
    return "You are exactly at the average of %.1f kg/day." % AVERAGE_DAILY_KG


def make_bar(value, largest, width=30):
    """Make a simple text bar like #######  for the chart."""
    if largest == 0:
        return ""
    length = int((value / largest) * width)
    return "#" * length


def get_tip(entries):
    """Give a tip based on the category with highest emission."""
    top = highest_category(entries)
    if top is None:
        return "Add some activities first to get personalised tips."
    return "Your biggest source is '%s'. Tip: %s" % (top, TIPS[top])


def trees_needed(total_kg):
    """
    Rough idea of how many trees are needed to absorb this CO2 in a year.
    One tree absorbs about 21 kg CO2 per year (commonly quoted estimate).
    """
    return round(total_kg / 21, 1)
