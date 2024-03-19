import re
OBESE_DECLARATORS_TOKENS: list = [
    'pregnancies', 'diagnosis', 'treatment',
    'glucose', 'bloodPressure', 'skinThickness',
    'insulin', 'bmi', 'diabetesPedigreeFunction',
    'age', 'outcome'
]

for declarator in OBESE_DECLARATORS_TOKENS:
    declarator_match = re.findall(r"\A\b{}\b".format(declarator), "pregnancies")
    print(declarator_match)