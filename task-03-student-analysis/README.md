# 📊 Task 3: Student Performance Data Analysis

## 🎯 Project Objective
Demonstrate core data engineering and analysis capabilities using Python and Pandas. The project handles data loading, discovery of missing values, numeric value imputation, logical data filtering, and departmental aggregations on a student performance dataset.

---

## 🛠️ Tech Stack & Requirements
* **Language:** Python 3.x
* **Core Library:** Pandas
* **Environment:** Jupyter Notebook Engine

---

## 🏗️ Data Pipeline Architecture

### 1. Ingestion & Structural Inspection
* Reads `students.csv` into a structured DataFrame.
* Discovers internal schema metrics using `.info()` and calculates missing data anomalies using `.isnull().sum()`.

### 2. Imputation (Data Cleaning)
* Targets structural missing boundaries dynamically.
* Resolves missing student grade metrics cleanly by imputing them with the global calculated mean score without discarding row data.

### 3. Logical Filtering & Aggregate Grouping
* Isolates high-proficiency student tiers with customized logic thresholds.
* Calculates departmental performance ratios using `.groupby()` aggregation pipelines.

---

## 📂 Repository Structure

```text
task-3-pandas-analysis/
│
├── students.csv
├── analysis.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Setup & Execution Guide

### 1. Install dependencies
```Bash
pip install -r requirements.txt
```

### 2. Launch the Environment
```Bash
jupyter notebook
```

### 3. Run Project
Open analysis.ipynb and run cells step by step..