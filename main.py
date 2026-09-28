"""
main.py
-------
Command line menu for the Digital Carbon Footprint Tracker.
Run with:  python main.py

Author: Vedaant Karande
"""

from datetime import date

import calculator
import storage
import analysis


def choose_from_list(title, options):
    """Show a numbered list and return the option the user picks."""
    print("\n" + title)
    for i, opt in enumerate(options, start=1):
        print("  %d. %s" % (i, opt))
    while True:
        choice = input("Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid choice, try again.")


def read_number(message):
    """Keep asking until the user types a valid non-negative number."""
    while True:
        text = input(message).strip()
        try:
            value = float(text)
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("That is not a number, try again.")


def add_activity():
    """Ask the user for an activity and save it."""
    category = choose_from_list("Choose a category:", calculator.get_categories())
    item = choose_from_list("Choose activity:", calculator.get_items(category))
    unit = calculator.get_unit(category, item)
    quantity = read_number("Enter amount in %s: " % unit)

    emission = calculator.calculate_emission(category, item, quantity)
    storage.add_entry(category, item, quantity, emission)
    print("\nSaved! %s %s of %s = %.3f kg CO2" % (quantity, unit, item, emission))


def show_today():
    """Show today's total and comparison with the average."""
    today = date.today().isoformat()
    entries = storage.load_entries()
    todays = analysis.filter_by_date(entries, today)

    print("\n--- Today's Summary (%s) ---" % today)
    if not todays:
        print("No activities added today.")
        return
    total = analysis.total_emission(todays)
    print("Total footprint today: %.3f kg CO2" % total)
    print(analysis.compare_with_average(total))


def show_category_report():
    """Show the category breakdown with a simple text bar chart."""
    entries = storage.load_entries()
    if not entries:
        print("\nNo data yet. Add some activities first.")
        return

    print("\nReport for: 1. This month   2. All time")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        month = date.today().strftime("%Y-%m")
        entries = analysis.filter_by_month(entries, month)
        heading = "This month (%s)" % month
    else:
        heading = "All time"

    totals = analysis.totals_by_category(entries)
    print("\n--- Category Report: %s ---" % heading)
    if not totals:
        print("No data for this period.")
        return

    largest = max(totals.values())
    for cat, value in totals.items():
        print("%-12s %8.2f kg  %s" % (cat, value, analysis.make_bar(value, largest)))

    grand = analysis.total_emission(entries)
    print("\nTotal: %.2f kg CO2" % grand)
    print("Trees needed to absorb this in a year: about %s" % analysis.trees_needed(grand))


def show_history():
    """Print every saved entry."""
    entries = storage.load_entries()
    print("\n--- History ---")
    if not entries:
        print("No entries yet.")
        return
    for e in entries:
        print("%s | %-11s | %-16s | %6s | %.3f kg" % (
            e["date"], e["category"], e["item"], e["quantity"], e["emission"]))


def show_tips():
    """Show a tip based on the user's data."""
    entries = storage.load_entries()
    print("\n--- Tip ---")
    print(analysis.get_tip(entries))


def reset_data():
    """Delete all data after confirmation."""
    answer = input("Delete ALL saved data? (yes/no): ").strip().lower()
    if answer == "yes":
        storage.clear_entries()
        print("All data deleted.")
    else:
        print("Cancelled.")


def main():
    print("=" * 45)
    print("   DIGITAL CARBON FOOTPRINT TRACKER")
    print("=" * 45)

    while True:
        print("\nMAIN MENU")
        print("  1. Add an activity")
        print("  2. Today's summary")
        print("  3. Category report")
        print("  4. View history")
        print("  5. Get a tip to reduce footprint")
        print("  6. Delete all data")
        print("  7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_activity()
        elif choice == "2":
            show_today()
        elif choice == "3":
            show_category_report()
        elif choice == "4":
            show_history()
        elif choice == "5":
            show_tips()
        elif choice == "6":
            reset_data()
        elif choice == "7":
            print("Thank you for caring about the planet. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
