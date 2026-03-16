# src/profile.py

# Main resume profile dictionary
resume_profile = {
    "name": "",
    "email": "",
    "contact_number": "",
    "education": "",
    "skills": []
}

def create_profile():
    """
    Collect user input for the main resume profile.
    Store inputs in the resume_profile dictionary.
    """
    resume_profile["name"] = input("Enter your full name: ")
    resume_profile["email"] = input("Enter your email address: ")
    resume_profile["contact_number"] = input("Enter your contact number: ")
    resume_profile["education"] = input("Enter your highest education: ")
    skills_input = input("Enter your skills (comma-separated): ")
    resume_profile["skills"] = [skill.strip() for skill in skills_input.split(",")]
    print("\nResume profile created successfully!")
    print(resume_profile)
