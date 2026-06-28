"""
Student Record Management System
==================================
Demonstrates: CSV file I/O, JSON file I/O, custom exceptions,
try/except/finally error handling, logging, and input validation.

Author: Henry
Course: BSE - File Handling & Exception Management
"""

import csv
import json
import logging
import os
import re
from datetime import datetime

# ─────────────────────────────────────────────
# FILE PATHS
# ─────────────────────────────────────────────
CSV_FILE  = "students.csv"
JSON_FILE = "students.json"
LOG_FILE  = "student_system.log"

# CSV columns (core academic info)
CSV_FIELDS = ["reg_number", "name", "age", "year", "gpa"]

# ─────────────────────────────────────────────
# LOGGING SETUP
# ─────────────────────────────────────────────
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def log(message: str, level: str = "info"):
    """Write a message to the log file."""
    if level == "error":
        logging.error(message)
    elif level == "warning":
        logging.warning(message)
    else:
        logging.info(message)


# ─────────────────────────────────────────────
# CUSTOM EXCEPTIONS
# ─────────────────────────────────────────────
class StudentNotFoundError(Exception):
    """Raised when a student registration number does not exist."""
    pass

class DuplicateStudentError(Exception):
    """Raised when trying to add a student whose reg number already exists."""
    pass

class InvalidInputError(Exception):
    """Raised when user input fails validation."""
    pass


# ─────────────────────────────────────────────
# FILE HELPERS
# ─────────────────────────────────────────────
def load_csv() -> list[dict]:
    """Load all student records from the CSV file.
    Returns an empty list if the file does not exist yet."""
    if not os.path.exists(CSV_FILE):
        return []
    try:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        log(f"Failed to read CSV: {e}", "error")
        print(f"  [Error] Could not read student file: {e}")
        return []


def save_csv(records: list[dict]):
    """Write all student records to the CSV file."""
    try:
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()
            writer.writerows(records)
    except Exception as e:
        log(f"Failed to write CSV: {e}", "error")
        raise


def load_json() -> dict:
    """Load additional student details from the JSON file.
    Returns an empty dict if the file does not exist."""
    if not os.path.exists(JSON_FILE):
        return {}
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        log(f"JSON decode error: {e}", "error")
        print(f"  [Warning] students.json appears corrupted. Starting fresh.")
        return {}
    except Exception as e:
        log(f"Failed to read JSON: {e}", "error")
        return {}


def save_json(data: dict):
    """Write additional student details to the JSON file."""
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        log(f"Failed to write JSON: {e}", "error")
        raise


# ─────────────────────────────────────────────
# INPUT VALIDATION HELPERS
# ─────────────────────────────────────────────
def validate_reg(reg: str) -> str:
    """Registration number must match pattern like 21/U/1234 or BSE2023001."""
    reg = reg.strip().upper()
    if not reg:
        raise InvalidInputError("Registration number cannot be empty.")
    return reg


def validate_name(name: str) -> str:
    name = name.strip().title()
    if len(name) < 2:
        raise InvalidInputError("Name must be at least 2 characters.")
    if not re.match(r"^[A-Za-z\s'\-]+$", name):
        raise InvalidInputError("Name must contain letters only.")
    return name


def validate_age(age_str: str) -> int:
    try:
        age = int(age_str.strip())
    except ValueError:
        raise InvalidInputError("Age must be a whole number.")
    if not (16 <= age <= 60):
        raise InvalidInputError("Age must be between 16 and 60.")
    return age


def validate_year(year_str: str) -> int:
    try:
        year = int(year_str.strip())
    except ValueError:
        raise InvalidInputError("Year of study must be a number.")
    if not (1 <= year <= 6):
        raise InvalidInputError("Year of study must be between 1 and 6.")
    return year


def validate_gpa(gpa_str: str) -> float:
    try:
        gpa = float(gpa_str.strip())
    except ValueError:
        raise InvalidInputError("GPA must be a decimal number.")
    if not (0.0 <= gpa <= 5.0):
        raise InvalidInputError("GPA must be between 0.0 and 5.0.")
    return round(gpa, 2)


def validate_phone(phone: str) -> str:
    phone = phone.strip()
    if not re.match(r"^\+?[0-9\s\-]{7,15}$", phone):
        raise InvalidInputError("Enter a valid phone number (digits, spaces, +, -).")
    return phone


# ─────────────────────────────────────────────
# CORE OPERATIONS
# ─────────────────────────────────────────────
def find_student(records: list[dict], reg: str) -> dict | None:
    """Return the CSV record for a student, or None if not found."""
    for r in records:
        if r["reg_number"].upper() == reg.upper():
            return r
    return None


def add_student():
    """Collect details and add a new student to both CSV and JSON."""
    print("\n  ── Add New Student ──")
    try:
        reg  = validate_reg(input("  Registration Number : "))
        name = validate_name(input("  Full Name           : "))
        age  = validate_age(input("  Age                 : "))
        year = validate_year(input("  Year of Study       : "))
        gpa  = validate_gpa(input("  GPA (0.0 – 5.0)     : "))

        # Additional details for JSON
        program = input("  Program/Course      : ").strip() or "Unknown"
        address = input("  Address             : ").strip() or "Not provided"
        phone   = validate_phone(input("  Phone Number        : "))
        email   = input("  Email               : ").strip() or "Not provided"

        records = load_csv()

        # Check for duplicate registration number
        if find_student(records, reg):
            raise DuplicateStudentError(
                f"A student with reg number '{reg}' already exists."
            )

        # Save to CSV
        records.append({
            "reg_number": reg,
            "name": name,
            "age": age,
            "year": year,
            "gpa": gpa,
        })
        save_csv(records)

        # Save extra details to JSON
        details = load_json()
        details[reg] = {
            "program": program,
            "address": address,
            "phone": phone,
            "email": email,
            "registered_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        save_json(details)

        print(f"\n  ✓ Student '{name}' ({reg}) added successfully.")
        log(f"Added student: {reg} – {name}")

    except (InvalidInputError, DuplicateStudentError) as e:
        print(f"\n  [Error] {e}")
        log(f"Add failed: {e}", "warning")
    except Exception as e:
        print(f"\n  [Unexpected Error] {e}")
        log(f"Unexpected error in add_student: {e}", "error")
    finally:
        # 'finally' always runs – useful for cleanup or audit trail
        log("add_student() function completed.")


def view_all_students():
    """Display all students from the CSV file in a simple table."""
    print("\n  ── All Students ──")
    try:
        records = load_csv()
        if not records:
            print("  No student records found.")
            log("Viewed all students – no records.")
            return

        # Print table header
        print(f"\n  {'Reg No':<15} {'Name':<25} {'Age':<5} {'Year':<6} {'GPA':<5}")
        print("  " + "─" * 60)

        for r in records:
            print(
                f"  {r['reg_number']:<15} {r['name']:<25} "
                f"{r['age']:<5} {r['year']:<6} {r['gpa']:<5}"
            )

        print(f"\n  Total: {len(records)} student(s)")
        log(f"Viewed all students – {len(records)} record(s) displayed.")

    except Exception as e:
        print(f"\n  [Error] Could not load students: {e}")
        log(f"Error in view_all_students: {e}", "error")
    finally:
        log("view_all_students() function completed.")


def search_student():
    """Search for a student by registration number and show full details."""
    print("\n  ── Search Student ──")
    try:
        reg = validate_reg(input("  Enter Registration Number: "))
        records = load_csv()
        student = find_student(records, reg)

        if not student:
            raise StudentNotFoundError(f"No student found with reg number '{reg}'.")

        # Fetch extra details from JSON
        details = load_json()
        extra = details.get(reg.upper(), details.get(reg, {}))

        print(f"\n  ┌── Student Record ───────────────────────┐")
        print(f"  │ Reg Number  : {student['reg_number']}")
        print(f"  │ Name        : {student['name']}")
        print(f"  │ Age         : {student['age']}")
        print(f"  │ Year        : {student['year']}")
        print(f"  │ GPA         : {student['gpa']}")
        if extra:
            print(f"  │ Program     : {extra.get('program', 'N/A')}")
            print(f"  │ Address     : {extra.get('address', 'N/A')}")
            print(f"  │ Phone       : {extra.get('phone', 'N/A')}")
            print(f"  │ Email       : {extra.get('email', 'N/A')}")
            print(f"  │ Registered  : {extra.get('registered_on', 'N/A')}")
        print(f"  └─────────────────────────────────────────┘")

        log(f"Searched for student: {reg}")

    except (InvalidInputError, StudentNotFoundError) as e:
        print(f"\n  [Error] {e}")
        log(f"Search failed: {e}", "warning")
    except Exception as e:
        print(f"\n  [Unexpected Error] {e}")
        log(f"Unexpected error in search_student: {e}", "error")
    finally:
        log("search_student() function completed.")


def update_student():
    """Update one or more fields for an existing student."""
    print("\n  ── Update Student ──")
    try:
        reg = validate_reg(input("  Enter Registration Number to update: "))
        records = load_csv()
        student = find_student(records, reg)

        if not student:
            raise StudentNotFoundError(f"No student found with reg number '{reg}'.")

        print(f"\n  Updating record for: {student['name']} ({reg})")
        print("  (Press Enter to keep the current value)\n")

        # Update CSV fields
        new_name = input(f"  Name [{student['name']}]   : ").strip()
        new_age  = input(f"  Age  [{student['age']}]    : ").strip()
        new_year = input(f"  Year [{student['year']}]   : ").strip()
        new_gpa  = input(f"  GPA  [{student['gpa']}]   : ").strip()

        if new_name:
            student["name"] = validate_name(new_name)
        if new_age:
            student["age"] = validate_age(new_age)
        if new_year:
            student["year"] = validate_year(new_year)
        if new_gpa:
            student["gpa"] = validate_gpa(new_gpa)

        save_csv(records)

        # Update JSON fields
        details = load_json()
        extra = details.get(reg, {})

        new_program = input(f"  Program [{extra.get('program', '')}] : ").strip()
        new_address = input(f"  Address [{extra.get('address', '')}] : ").strip()
        new_phone   = input(f"  Phone   [{extra.get('phone', '')}]   : ").strip()
        new_email   = input(f"  Email   [{extra.get('email', '')}]   : ").strip()

        if new_program: extra["program"] = new_program
        if new_address: extra["address"] = new_address
        if new_phone:   extra["phone"]   = validate_phone(new_phone)
        if new_email:   extra["email"]   = new_email

        details[reg] = extra
        save_json(details)

        print(f"\n  ✓ Student '{student['name']}' updated successfully.")
        log(f"Updated student: {reg}")

    except (InvalidInputError, StudentNotFoundError) as e:
        print(f"\n  [Error] {e}")
        log(f"Update failed: {e}", "warning")
    except Exception as e:
        print(f"\n  [Unexpected Error] {e}")
        log(f"Unexpected error in update_student: {e}", "error")
    finally:
        log("update_student() function completed.")


def delete_student():
    """Remove a student record from both CSV and JSON files."""
    print("\n  ── Delete Student ──")
    try:
        reg = validate_reg(input("  Enter Registration Number to delete: "))
        records = load_csv()
        student = find_student(records, reg)

        if not student:
            raise StudentNotFoundError(f"No student found with reg number '{reg}'.")

        # Confirm before deleting
        confirm = input(
            f"\n  Are you sure you want to delete '{student['name']}' ({reg})? (yes/no): "
        ).strip().lower()

        if confirm != "yes":
            print("  Deletion cancelled.")
            log(f"Deletion cancelled for: {reg}")
            return

        # Remove from CSV
        records = [r for r in records if r["reg_number"].upper() != reg.upper()]
        save_csv(records)

        # Remove from JSON
        details = load_json()
        if reg in details:
            del details[reg]
            save_json(details)

        print(f"\n  ✓ Student '{student['name']}' deleted successfully.")
        log(f"Deleted student: {reg} – {student['name']}")

    except (InvalidInputError, StudentNotFoundError) as e:
        print(f"\n  [Error] {e}")
        log(f"Delete failed: {e}", "warning")
    except Exception as e:
        print(f"\n  [Unexpected Error] {e}")
        log(f"Unexpected error in delete_student: {e}", "error")
    finally:
        log("delete_student() function completed.")


# ─────────────────────────────────────────────
# MENU
# ─────────────────────────────────────────────
def print_menu():
    print("\n" + "=" * 45)
    print("    STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 45)
    print("  1. Add New Student")
    print("  2. View All Students")
    print("  3. Search Student by Reg Number")
    print("  4. Update Student Details")
    print("  5. Delete Student Record")
    print("  6. Exit")
    print("=" * 45)


def main():
    """Entry point – runs the menu loop."""
    log("=" * 40)
    log("System started.")

    while True:
        print_menu()
        choice = input("  Enter your choice (1–6): ").strip()

        if choice == "1":
            log("User selected: Add Student")
            add_student()
        elif choice == "2":
            log("User selected: View All Students")
            view_all_students()
        elif choice == "3":
            log("User selected: Search Student")
            search_student()
        elif choice == "4":
            log("User selected: Update Student")
            update_student()
        elif choice == "5":
            log("User selected: Delete Student")
            delete_student()
        elif choice == "6":
            print("\n  Goodbye! System shutting down.\n")
            log("System exited by user.")
            break
        else:
            print("  [Invalid] Please enter a number from 1 to 6.")
            log(f"Invalid menu choice: '{choice}'", "warning")


if __name__ == "__main__":
    main()
