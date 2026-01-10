
from __future__ import annotations
import json
from pathlib import Path
from getpass import getpass
from datetime import datetime
import time
from typing import Optional, Dict, Any

PROFILES_FILE = Path(__file__).parent / "profiles.json"


def load_profiles() -> Dict[str, Any]:
    if not PROFILES_FILE.exists():
        return {}
    try:
        with open(PROFILES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_profiles(profiles: Dict[str, Any]) -> None:
    with open(PROFILES_FILE, "w", encoding="utf-8") as f:
        json.dump(profiles, f, indent=2, ensure_ascii=False)


def prompt_password_creation() -> str:
    """Ask the user to create and confirm a password. Returns the created password."""
    print("Create a secure password (input hidden). Press Ctrl-C to cancel.")
    while True:
        pw = getpass("New password: ")
        if not pw:
            print("Password cannot be empty. Try again.")
            continue
        pw2 = getpass("Confirm password: ")
        if pw != pw2:
            print("Passwords do not match. Try again.\n")
            continue
        print("Password successfully created!\n")
        return pw


def prompt_login(expected_password: str, max_attempts: int = 5) -> bool:
    print("----- LOGIN -----")
    attempts = 0
    while attempts < max_attempts:
        try:
            entered = getpass("Enter your password: ")
        except KeyboardInterrupt:
            print("\nLogin cancelled")
            return False
        if entered == expected_password:
            print("Login successful!\n")
            return True
        attempts += 1
        print(f"Incorrect password ({attempts}/{max_attempts}). Try again.\n")
    print("Maximum attempts reached. Exiting login.")
    return False


def input_nonempty(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Input cannot be empty. Please try again.")


def input_int(prompt: str, min_val: Optional[int] = None, max_val: Optional[int] = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if min_val is not None and val < min_val:
            print(f"Value must be >= {min_val}.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be <= {max_val}.")
            continue
        return val


def input_float(prompt: str, min_val: Optional[float] = None, max_val: Optional[float] = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Please enter a valid number (e.g., 3.5).")
            continue
        if min_val is not None and val < min_val:
            print(f"Value must be >= {min_val}.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be <= {max_val}.")
            continue
        return val


def countdown(seconds: int = 5) -> None:
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)


def create_or_edit_profile(username: str, profiles: Dict[str, Any]) -> Dict[str, Any]:
    print("Let's create your profile. Press Enter to keep an existing value.")
    existing = profiles.get(username, {})
    name = input_nonempty(f"Full name [{existing.get('name', '')}]: ") if not existing.get('name') else input(f"Full name [{existing.get('name')}]: ") or existing.get('name')
    age = None
    if existing.get('age') is not None:
        raw_age = input(f"Age [{existing.get('age')}]: ")
        age = int(raw_age) if raw_age.strip() else existing.get('age')
    else:
        age = input_int("Age: ", min_val=0, max_val=150)

    gpa = None
    if existing.get('gpa') is not None:
        raw_gpa = input(f"GPA [{existing.get('gpa')}]: ")
        gpa = float(raw_gpa) if raw_gpa.strip() else existing.get('gpa')
    else:
        gpa = input_float("GPA (e.g., 3.5): ", min_val=0.0, max_val=4.0)

    profile = {
        "name": name,
        "age": int(age),
        "gpa": float(gpa),
        "student": True,
        "updated": datetime.utcnow().isoformat() + "Z",
    }
    profiles[username] = profile
    save_profiles(profiles)
    print("Profile saved.\n")
    return profile


def main() -> None:
    try:
        profiles = load_profiles()

        print("Welcome — a friendly interactive profile creator!")
        # username to index profiles; allow multiple users per file
        username = input_nonempty("Choose a username (no spaces): ")

        if username in profiles:
            print(f"Existing profile found for '{username}'. You will need the saved password to log in.")
            expected_pw = profiles[username].get("password")
            if not expected_pw:
                print("No password previously stored for this user. Creating a new password.")
                pw = prompt_password_creation()
                profiles[username]["password"] = pw
                save_profiles(profiles)
                expected_pw = pw
        else:
            print(f"No profile found for '{username}'. Creating account.")
            pw = prompt_password_creation()
            profiles[username] = {"password": pw}
            save_profiles(profiles)
            expected_pw = pw

        ok = prompt_login(expected_pw)
        if not ok:
            return

        # short celebratory countdown
        countdown(3)
        print("\n\n----- PROFLE SECTION -----\n\n")

        # If profile missing fields, prompt to create/edit them
        profile = profiles.get(username, {})
        if not profile.get("name") or not profile.get("age") or not profile.get("gpa"):
            profile = create_or_edit_profile(username, profiles)

        # Main menu loop
        while True:
            print("\nMain menu:\n 1) View profile\n 2) Edit profile\n 3) Logout and switch user\n 4) Exit")
            choice = input("Choose an option [1-4]: ").strip()
            if choice == "1":
                p = profiles.get(username, {})
                print("\n--- Profile ---")
                print(f"Username: {username}")
                print(f"Name: {p.get('name')}")
                print(f"Age: {p.get('age')}")
                print(f"GPA: {p.get('gpa')}")
                print(f"Student: {p.get('student')}")
                print(f"Last updated: {p.get('updated')}")
            elif choice == "2":
                profile = create_or_edit_profile(username, profiles)
            elif choice == "3":
                print("Logging out...\n")
                main()  # start over for a new user
                return
            elif choice == "4":
                print("Goodbye — stay productive!")
                return
            else:
                print("Invalid choice. Please select 1-4.")

    except KeyboardInterrupt:
        print("\nInterrupted. Exiting gracefully.")


if __name__ == "__main__":
    main()
