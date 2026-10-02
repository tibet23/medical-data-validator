from src.validator import find_invalid_records, validate

# Sample valid record template
VALID_RECORD = {
    'patient_id': 'P1001',
    'age': 34,
    'gender': 'Female',
    'diagnosis': 'Hypertension',
    'medications': ['Lisinopril'],
    'last_visit_id': 'V2301'
}

def test_find_invalid_records_with_valid_data():
    """Test that a completely valid record returns no invalid keys."""
    invalid_keys = find_invalid_records(**VALID_RECORD)
    assert invalid_keys == []

def test_invalid_age():
    """Test that an age under 18 fails validation."""
    record = VALID_RECORD.copy()
    record['age'] = 16
    invalid_keys = find_invalid_records(**record)
    assert 'age' in invalid_keys

def test_invalid_patient_id():
    """Test that a patient_id missing the 'P' prefix fails validation."""
    record = VALID_RECORD.copy()
    record['patient_id'] = '1001'
    invalid_keys = find_invalid_records(**record)
    assert 'patient_id' in invalid_keys

def test_validate_success():
    """Test that validate() returns True on a clean dataset."""
    assert validate([VALID_RECORD]) is True

def test_validate_invalid_top_level_structure():
    """Test that validate() returns False if input is not a list or tuple."""
    assert validate("invalid_string_input") is False