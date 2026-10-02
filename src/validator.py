from src.schema import PATIENT_ID_REGEX, VISIT_ID_REGEX, REQUIRED_KEYS, VALID_GENDERS, MIN_AGE

def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
        'patient_id': isinstance(patient_id, str) and bool(PATIENT_ID_REGEX.fullmatch(patient_id)),
        'age': isinstance(age, int) and age >= MIN_AGE,
        'gender': isinstance(gender, str) and gender.lower() in VALID_GENDERS,
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        'medications': isinstance(medications, list) and all(isinstance(i, str) for i in medications),
        'last_visit_id': isinstance(last_visit_id, str) and bool(VISIT_ID_REGEX.fullmatch(last_visit_id))
    }
    return [key for key, value in constraints.items() if not value]

def validate(data):
    if not isinstance(data, (list, tuple)):
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False
    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        if set(dictionary.keys()) != REQUIRED_KEYS:
            print(f'Invalid format: record at position {index} has missing/invalid keys.')
            is_invalid = True
            continue

        invalid_records = find_invalid_records(**dictionary)
        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True

    if is_invalid:
        return False
    print('Valid format.')
    return True