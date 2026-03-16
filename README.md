# Resume Tracker

## Overview
**Resume Tracker** is a command-line interface (CLI) tool designed for job seekers to **efficiently manage and organize their resumes**. Users can create a base resume profile, maintain multiple versions tailored for specific job applications, and track their job application history in a structured and professional way.

This project demonstrates **Python programming, data handling, and CLI development** with a focus on creating real-world, useful tools for career management.

---

## Features
- **Create Base Resume Profile:** Store personal information such as name, email, contact number, education, and skills.
- **Add Resume Versions:** Create multiple resume versions tailored to specific job applications.
- **List Resume Versions:** View all resume versions with detailed information including job title, company, applied date, highlighted skills, and notes.
- **Update Resume Versions:** Modify any existing resume version easily.
- **User-Friendly CLI Menu:** Simple and intuitive interface to navigate all options.
- **Exit Gracefully:** Program closes with a professional thank-you message.

---

## Repository Structure
```text
resume-tracker/
├── data/                # Store future data files (JSON, CSV, etc.)
│   └── .gitkeep         # Placeholder
├── src/                 # Source code
│   ├── main.py          # CLI menu
│   ├── profile.py       # Resume profile functions
│   └── version.py       # Resume version functions
├── tests/               # Optional unit tests
│   └── .gitkeep
└── README.md            # Project documentation
