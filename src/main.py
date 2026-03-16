# src/main.py

from profile import create_profile
from version import add_resume_version, list_resume_versions, update_resume_version

def main():
    while True:
        print("\n=== Resume Tracker Menu ===")
        print("1. Create Resume Profile")
        print("2. Add Resume Version")
        print("3. List Resume Versions")
        print("4. Update Resume Version")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_profile()
        elif choice == "2":
            add_resume_version()
        elif choice == "3":
            list_resume_versions()
        elif choice == "4":
            update_resume_version()
        elif choice == "5":
            print("\nThank you for using Resume Tracker! Goodbye.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
