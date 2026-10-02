# 🏥 Medical Data Validator (Med-Data Validator)

A modular Python data validation system designed to inspect and sanitize patient medical records. Built as part of a freeCodeCamp interactive Python workshop.

---

## 📌 Project Overview

The Med-Data Validator ensures that medical datasets conform to strict schema and data typing standards before processing. It checks sequence types, dictionary structures, field presence, and field-level constraints using Regular Expressions and type enforcement.

---

## 🛠️ Project Structure

med-data-validator/
│
├── src/
│   ├── __init__.py
│   ├── schema.py          # Regex patterns, constants, and schema rules
│   └── validator.py       # Core validation logic
│
├── tests/
│   └── test_validator.py  # pytest test suite
│
├── app.py                 # Interactive Streamlit web interface
├── main.py                # Command Line Interface (CLI) entry point
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

---

## 📋 Data Validation Rules

* patient_id: String | Case-insensitive match for 'P' followed by digits (e.g., P1001)
* age: Integer | Must be >= 18 years old
* gender: String | Case-insensitive match for 'Male' or 'Female'
* diagnosis: String or None | Patient diagnosis details
* medications: List | Must be a list containing only strings
* last_visit_id: String | Case-insensitive match for 'V' followed by digits (e.g., V2301)

---

## 🚀 Getting Started

### 1. Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/Med-Data_Validator.git
cd Med-Data_Validator
pip install -r requirements.txt

### 2. Run Command Line Interface (CLI)

To test validation on the sample dataset in main.py:

python main.py

### 3. Launch Web Interface (Streamlit)

To open the interactive browser app:

streamlit run app.py

### 4. Run Unit Tests

To run the test suite:

pytest

---

## 💡 How It Works (Step 44 Logic)

1. Schema Check: Confirms input data is a list of dictionaries with expected key sets.
2. Error Collection: find_invalid_records() evaluates each patient record against key constraints and returns a list of failed field names.
3. Targeted Reporting: The validate() loop iterates through error keys, pulls breaking values (dictionary[key]), and prints explicit field errors with index positions.