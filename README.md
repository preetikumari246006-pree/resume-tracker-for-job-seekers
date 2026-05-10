# 📄 Resume Tracker

> A lightweight CLI tool to create, manage, and track multiple resume versions for job applications efficiently.

---

## 📌 Overview

**Resume Tracker** is a command-line interface (CLI) application designed to help job seekers organize their resumes and job applications in a structured and efficient way.

It allows users to maintain a base resume profile, generate multiple tailored versions for different roles, and track application history — all from the terminal.

This project demonstrates practical use of **Python programming**, **file-based data management**, and **CLI system design**, focused on solving real-world career organization challenges.

---

## 🎯 Key Features

- 👤 **Create Base Resume Profile**  
  Store essential details such as name, email, contact number, education, and skills.

- 📝 **Manage Resume Versions**  
  Create multiple tailored resumes for different job roles and companies.

- 📋 **View Resume History**  
  Display all saved resume versions with:
  - Job title  
  - Company name  
  - Application date  
  - Skills highlighted  
  - Additional notes  

- ✏️ **Update Existing Entries**  
  Modify and keep resume versions up to date with ease.

- 🧭 **Interactive CLI Menu**  
  Simple and structured terminal-based navigation system.

- 🚪 **Clean Exit Handling**  
  Graceful termination with user-friendly messages.

---

## 🗂️ Project Structure

```text
resume-tracker/
├── data/                 # Data storage (JSON / CSV files)
│   └── .gitkeep
├── src/                  # Source code
│   ├── main.py           # CLI entry point
│   ├── profile.py        # Resume profile logic
│   └── version.py        # Resume version management
├── tests/                # Unit tests (optional)
│   └── .gitkeep
└── README.md             # Project documentation
