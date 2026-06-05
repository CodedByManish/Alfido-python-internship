# 🌐 Task 4 - Student Records Registry (Flask & MySQL CRUD)

## 🎯 Goal
Build a functional, responsive web application demonstrating backend fundamentals, dynamic HTTP routing, database management, and safe form data processing.

---

## 📂 Project Overview
This web application provides a secure portal to manage student tracking records. It utilizes Flask for the backend model-view-controller pipeline, communicates with a MySQL database via relational SQL transactions, and renders an elegant, mobile-first frontend user interface styled with the Bootstrap framework.

---

## ✨ Features
* **Dynamic Data Read (GET):** Extracts existing student profiles dynamically from MySQL and displays them inside an interactive, structured tracking table.
* **Data Injection (POST):** Implements server-validated web forms to append new student data strings directly into the relational state.
* **State Purging (Delete):** Safe individual deletion pathways to clear targeted entries cleanly using URL routing variables.
* **Flash Notifications:** Returns real-time, color-coded status alerts (Success, Warning, Danger) directly onto the client viewport upon transaction completions.

---

## 📁 Project Directory Layout
```text
task-4-flask-crud/
│
├── templates/
│   ├── base.html         # Main Bootstrap core wrapper layout
│   ├── index.html        # Interactive directory dashboard table
│   └── add_student.html  # Standard POST form validation page
│
├── .env                  # Hidden local environment configurations
├── .gitignore            # Version control exclusion rules
├── app.py                # Main backend controller and SQL routing logic
├── requirements.txt      # Pinpointed external module dependencies
└── schema.sql            # Raw database schema initialization scripts
```