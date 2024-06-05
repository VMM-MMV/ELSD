from Parser import *
import os
import textwrap
parser: Parser = Parser()
    
class Compiler:
    def getIndent(self, indent):
        return " " * indent
    def ClassMethods(self, indent):
        code_block = """
def to_dict(self):
    # Initialize an empty dictionary to hold the structured data
    data = {}

    # Iterate over the instance's __dict__ to populate the structured dictionary
    for key, value in self.__dict__.items():
        if (key!="target" and key!="data_path"):
            # Transform the key to match the desired format and add the value wrapped in another dictionary
            transformed_key = f"{key[0].upper()+key[1:]}" if key!= "bmi" else key.upper()
            data[transformed_key] = {str(0): value}

    return data

def visualize(self):
    print("Here Add Vizualization Type Stuff or not")

def predict(self):
    data = self.to_dict()

    # Make the POST request with the correct content type
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

    # Print the response
    status = "Sick"
    if float(response.text[1:-2]) < 0.5:
        status = "Healthy"
    print("    The person is",status)

def load(self,path):
    df= pd.read_csv(path)
    new_df=df.copy()
    data= pd.DataFrame.to_json(df)
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

    result=response.text.replace("[","").replace("]","").split()
    dic={k:result[k] for k in range(len(result))}
    for i in dic: 
        status = "Sick"
        if float(dic[i]) < 0.5:
            status = "Healthy"
        print(f"The person {i} is {status}")


    df2=new_df.assign(Outcome=[round(float(x)) for x in result])
    df2.to_csv("Output.csv")
    print("Results saved in Output.csv")
    return 0
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
    
    def handleClassCreation(self, node, indent):
        class_code = "\n" + self.getIndent(indent) + "import pandas as pd \nimport json\nimport requests\nurl = 'https://94e4-35-194-229-90.ngrok-free.app/'\nclass " + node["name"] + ":" + "\n"
        indent += 4
        class_parameters_code = self.getIndent(indent) + "def __init__(self"
        class_body_code = ""
        indent += 3

        for parameter in node["parameters"]:
            parameters = self.handleVariableDeclaration(parameter, indent)
            var_name, var_type = [x.strip() for x in parameters.split(" = ")]
            class_parameters_code += f", {var_name}: {var_type} = 0"
            class_body_code += "\n" + self.getIndent(indent+1) + f"self.{var_name} = {var_type}({var_name})"
            
        target = self.handleVariableDeclaration(node["target"], indent)
        var_name, var_type = [x.strip() for x in target.split(" = ")]
        # TODO add vartype to check which type of regression to do
        # int thefore logistic, float linear
        class_parameters_code += f", {var_name} = None"
        class_body_code += "\n" + self.getIndent(indent+1) + f"self.target: {var_type} = '{var_name}'"

        class_body_code += "\n" + self.getIndent(indent+1) + f"self.data_path = str(r{node['data_path']})"
        
        class_parameters_code += "):"
        class_code += class_parameters_code + "\n"
        class_code += class_body_code + "\n"
        class_code += self.ClassMethods(indent=indent-3)
        templates_path = "Templates"

        if not os.path.exists(templates_path):
            os.mkdir(templates_path)
            os.mknod(templates_path+"/__init__.py")

        with open(f"{templates_path}/{node['name']}.py", "w+") as f:
            f.write(class_code)
        return class_code

    def handleClassInitialization(self, node, indent):
        class_init_code = f"from Templates.{node['class_type']} import * \n"
        class_init_code += f"{node['name']} = {node['class_type']}("

        indent += 3
        if (node["declarations"]):
            for parameter in node["declarations"]:
                parameters = self.handleVariableDeclaration(parameter, indent)
                var_name, var_type = [x.strip() for x in parameters.split(" = ")]
                class_init_code += f"{var_name} = {var_type}, "
            class_init_code = class_init_code[:-2]

        class_init_code += ")"
        return class_init_code
    
    def handleMethodCall(self, node, indent):
        return self.getIndent(indent) + f"{node['class_type']}.{node['method_name']}({node['parameters']})"
        
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
                self.code += self.getIndent(indent) + str(self.handleClassCreation(node, indent))
                return

            if node["type"] == "NewStruct":
                self.code += "\n"
                self.code += self.getIndent(indent) + str(self.handleClassInitialization(node, indent))
                return
            
            if node["type"] == "MethodCall":
                self.code += "\n"
                self.code += self.getIndent(indent) + str(self.handleMethodCall(node, indent))
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