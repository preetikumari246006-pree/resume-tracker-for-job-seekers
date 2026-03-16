# src/version.py

# List to store all resume versions
resume_versions = []

def add_resume_version():
    """
    Add a new resume version for a specific job application.
    """
    job_title = input("Enter the job title: ")
    company_name = input("Enter the company name: ")
    date_applied = input("Enter the date applied (YYYY-MM-DD): ")
    skills_input = input("Enter highlighted skills (comma-separated, optional): ")
    skills = [skill.strip() for skill in skills_input.split(",")] if skills_input else []
    notes = input("Enter notes or version description (optional): ")

    version = {
        "job_title": job_title,
        "company_name": company_name,
        "date_applied": date_applied,
        "skills": skills,
        "notes": notes
    }

    resume_versions.append(version)
    print("\nResume version added successfully!")

def list_resume_versions():
    """
    Display all resume versions in detail.
    """
    if not resume_versions:
        print("\nNo resume versions found.")
        return

    for idx, version in enumerate(resume_versions, 1):
        print(f"\nVersion {idx}:")
        print(f"Job Title: {version['job_title']}")
        print(f"Company: {version['company_name']}")
        print(f"Date Applied: {version['date_applied']}")
        print(f"Skills: {', '.join(version['skills']) if version['skills'] else 'None'}")
        print(f"Notes: {version['notes'] if version['notes'] else 'None'}")

def update_resume_version():
    """
    Update an existing resume version.
    """
    if not resume_versions:
        print("\nNo resume versions found to update.")
        return

    list_resume_versions()
    idx = int(input("\nEnter the version number to update: ")) - 1
    if idx < 0 or idx >= len(resume_versions):
        print("Invalid version number.")
        return

    version = resume_versions[idx]
    print("\nPress Enter to skip updating a field.")

    new_job_title = input(f"Job Title [{version['job_title']}]: ") or version['job_title']
    new_company = input(f"Company Name [{version['company_name']}]: ") or version['company_name']
    new_date = input(f"Date Applied [{version['date_applied']}]: ") or version['date_applied']
    new_skills_input = input(f"Skills [{', '.join(version['skills'])}]: ")
    new_skills = [skill.strip() for skill in new_skills_input.split(",")] if new_skills_input else version['skills']
    new_notes = input(f"Notes [{version['notes']}]: ") or version['notes']

    resume_versions[idx] = {
        "job_title": new_job_title,
        "company_name": new_company,
        "date_applied": new_date,
        "skills": new_skills,
        "notes": new_notes
    }

    print("\nResume version updated successfully!")
