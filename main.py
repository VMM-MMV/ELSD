from Parser import *
import json
parser: Parser = Parser()
code: str = r"""
declare Person = Obesity {
    jora: 2 + 3
    vova: "vova"
}
# Create Template {
#     name: Obesity
#     params: {
#         pregnancies: int
#         glucose: float
#         # bloodPressure: float
#         # skinThickness: float
#         # insulin: float
#         # bmi: float
#         # age: float
#     }
#     target: {diagnosis: float}
#     data: "C:\Users\Jora\Medic"
# }

vova = "6"
"""
result: dict = parser.parse(code)

print(json.dumps(result, indent=2)) 

# tokenizer: Tokenizer = Tokenizer(code)

# print(tokenizer.seeNthNextToken(1))
 

# declare Person = Obesity {
#     jora: 2
#     vova: "vova"
# }

# Person.hello