import re

PATIENT_ID_REGEX = re.compile(r'p\d+', re.IGNORECASE)
VISIT_ID_REGEX = re.compile(r'v\d+', re.IGNORECASE)
REQUIRED_KEYS = {'patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'}
VALID_GENDERS = ('male', 'female')
MIN_AGE = 18