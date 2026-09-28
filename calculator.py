"""
calculator.py  (Module 1)
-------------------------
Holds the emission factors and does the CO2 calculation.

An emission factor tells us how many kg of CO2 (CO2-equivalent) are
released for one unit of an activity. Example: driving a petrol car
for 1 km releases about 0.192 kg CO2.

NOTE: These values are approximate averages taken from public sources
(IPCC / CEA India / DEFRA style data). They are meant for learning and
awareness, not for official carbon accounting.
"""

# category -> item -> (emission factor in kg CO2 per unit, unit name)
EMISSION_FACTORS = {
    "transport": {
        "car":        (0.192, "km"),
        "motorbike":  (0.103, "km"),
        "bus":        (0.089, "km"),
        "train":      (0.041, "km"),
        "metro":      (0.030, "km"),
        "flight":     (0.255, "km"),
        "cycle/walk": (0.000, "km"),
    },
    "electricity": {
        # Indian grid average is roughly 0.82 kg CO2 per kWh
        "electricity": (0.82, "kWh"),
    },
    "food": {
        "vegetarian meal": (0.7, "meal"),
        "egg meal":        (1.0, "meal"),
        "chicken meal":    (1.8, "meal"),
        "mutton meal":     (5.0, "meal"),
    },
    "cooking_gas": {
        "LPG": (2.98, "kg"),
    },
    "waste": {
        "household waste": (0.5, "kg"),
    },
}


def get_categories():
    """Return the list of category names."""
    return list(EMISSION_FACTORS.keys())


def get_items(category):
    """Return the list of activities inside a category."""
    return list(EMISSION_FACTORS[category].keys())


def get_unit(category, item):
    """Return the unit (km, kWh, meal, kg) used for an activity."""
    return EMISSION_FACTORS[category][item][1]


def calculate_emission(category, item, quantity):
    """
    Calculate kg of CO2 for an activity.
    emission = quantity x emission factor
    """
    if category not in EMISSION_FACTORS:
        raise ValueError("Unknown category: " + str(category))
    if item not in EMISSION_FACTORS[category]:
        raise ValueError("Unknown activity: " + str(item))
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    factor = EMISSION_FACTORS[category][item][0]
    return round(quantity * factor, 3)
