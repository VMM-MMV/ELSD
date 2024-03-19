from Parser import *
import json
parser: Parser = Parser()
code: str = '''
Obesity {
    pregnancies : (1+2),
    diagnosis : 2,
    treatment : 2,
    glucose : 2,
    bloodPressure : 2,
    skinThickness : 2,
    insulin : 2,
    bmi : 2,
    diabetesPedigreeFunction : 2,
    age : (2+3)*2,
}'''

result: dict = parser.parse(code)

print(json.dumps(result, indent=2)) 