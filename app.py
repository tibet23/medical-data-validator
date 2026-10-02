import json
import streamlit as st
from src.validator import find_invalid_records, REQUIRED_KEYS

st.set_page_config(page_title="Med-Data Validator", page_icon="🏥", layout="centered")

st.title("🏥 Medical Data Validator")
st.write("Inspect and sanitize patient medical records according to project constraints.")

# Sample data for immediate testing
sample_data = [
    {
        "patient_id": "P1001",
        "age": 34,
        "gender": "Female",
        "diagnosis": "Hypertension",
        "medications": ["Lisinopril"],
        "last_visit_id": "V2301"
    },
    {
        "patient_id": "P1002",
        "age": 16,  # Invalid age (< 18)
        "gender": "Male",
        "diagnosis": "Asthma",
        "medications": ["Albuterol"],
        "last_visit_id": "INVALID_ID"  # Invalid ID format
    }
]

raw_input = st.text_area(
    "Paste Medical Records (JSON Format)",
    value=json.dumps(sample_data, indent=2),
    height=280
)

if st.button("Validate Dataset", type="primary"):
    try:
        data = json.loads(raw_input)
    except json.JSONDecodeError as e:
        st.error(f"Invalid JSON format: {e}")
        st.stop()

    if not isinstance(data, (list, tuple)):
        st.error("Invalid format: Top-level data must be a list of records.")
        st.stop()

    has_errors = False

    for index, record in enumerate(data):
        if not isinstance(record, dict):
            st.error(f"Position {index}: Item is not a valid dictionary object.")
            has_errors = True
            continue

        if set(record.keys()) != REQUIRED_KEYS:
            st.error(f"Position {index}: Missing or invalid keys in record schema.")
            has_errors = True
            continue

        invalid_keys = find_invalid_records(**record)

        if invalid_keys:
            has_errors = True
            for key in invalid_keys:
                st.warning(f"Field failure on `{key}` at record #{index}: Value `{record[key]}` breaks validation rules.")

    if not has_errors:
        st.balloons()
        st.success("🎉 Dataset passed all validation checks!")
    else:
        st.error("⚠️ Validation completed with errors.")