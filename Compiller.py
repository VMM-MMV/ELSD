from temp import *
import json
import textwrap
parser: Parser = Parser()
code: str = r"""
Create Template {
    name: Obesity
    params: {
        pregnancies: int
        glucose: float
        bloodPressure: float
        skinThickness: float
        insulin: float
        bmi: float
        age: float
    }
    target: {diagnosis: float}
    data: "C:\Users\Jora\Medic"
}
"""
result: dict = parser.parse(code)
    
class Compiler:
    def getIndent(self, indent):
        return " " * indent
    def ClassMethods(self, indent):
        code_block = """
def visualize(self):
    return "Here Add Vizualization Type Stuff"

def predict(self):
    return "Here Add Data Science Type Stuff"

def load(self)
    return pd.load(self.data_path)
    
"""

        indented_code_block = textwrap.indent(code_block, prefix=" " * indent)
        return self.getIndent(indent) + indented_code_block 

    def handleBinaryExpression(self, node):
        if not node:
            return
        
        if node.get("expression"):
            node = node["expression"]

        if node["type"] == "BinaryExpression":
            return f"({self.handleBinaryExpression(node['left'])} {self.handleBinaryExpression(node['operator'])} {self.handleBinaryExpression(node['right'])})"
        else:
            return str(node["value"])
    
    def handleVariableDeclaration(self, node, indent):
        node = node["declarations"]
        return self.getIndent(indent) + f"{node['id']['value']} = {self.handleBinaryExpression(node['init'])}"
    
    def handleClassInitialization(self, node, indent):
        class_code = "\n" + self.getIndent(indent) + "class " + node["name"] + ":" + "\n"
        indent += 2
        class_parameters_code = self.getIndent(indent) + "def __init__(self"
        class_body_code = ""
        indent += 2
        for parameter in node["parameters"]:
            parameters = self.handleVariableDeclaration(parameter, indent)
            var_name, var_type = [x.strip() for x in parameters.split(" = ")]
            class_parameters_code += f", {var_name}: {var_type}"
            class_body_code += "\n" + self.getIndent(indent+1) + f"self.{var_name} = {var_type}({var_name})"
            
        target = self.handleVariableDeclaration(node["target"], indent)
        var_name, var_type = [x.strip() for x in target.split(" = ")]
        class_parameters_code += f", {var_name}: {var_type}"
        class_body_code += "\n" + self.getIndent(indent+1) + f"self.target = {var_type}({var_name})"

        class_body_code += "\n" + self.getIndent(indent+1) + f"self.data_path = str({node['data_path']})"
        
        class_parameters_code += "):"
        class_code += class_parameters_code + "\n"
        class_code += class_body_code + "\n"
        class_code += self.ClassMethods(indent=indent-2)
        return class_code
        # print(class_code)

        
    def handleBlock(self, node, indent):
        self.code = ""
        def walkAst(node, indent):
            if not node:
                return

            # try:
            #     # print(node['type'])
            # except:
            #     pass
            
            if node["type"] == "ExpressionStatement":
                self.code += "\n"
                self.code += self.getIndent(indent) + str(self.handleBinaryExpression(node))
                return

            if node["type"] == "InitStruct":
                self.code += "\n"
                self.code += self.getIndent(indent) + str(self.handleClassInitialization(node, indent))
                return
            
            if node["type"] == "VariableDeclaration":
                self.code += "\n"
                self.code += self.getIndent(indent) + str(self.handleVariableDeclaration(node, indent))
            
            if node["type"] == "PrintStatement":
                self.code += "\n"
                self.code += self.getIndent(indent) + f"print({self.handleBinaryExpression(node)})"
                
            for key, value in node.items():
                if key != 'type' and isinstance(value, dict):
                    walkAst(value, indent)  # Child node
                elif key != 'type' and isinstance(value, list):
                    for item in value:
                        walkAst(item, indent)  # Items within a list            
            
        walkAst(node, indent)
        return self.code

compiler = Compiler()
code = compiler.handleBlock(result, 0)
print(code)