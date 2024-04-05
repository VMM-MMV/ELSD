from Tokenizer import *

class Parser:
    def parse(self, string: str) -> dict:
        self._string: str = string
        self._tokenizer: Tokenizer = Tokenizer(string)
        self._lookahead: dict | None = self._tokenizer.getNextToken()

        return self.Program()
    
    # Program : Obesity
    def Program(self) -> dict:
        return {
            "type": "Program",
            "body": self.StatementList()
        }
    
    
    # StatementList : Statement | StatementList Statement | None
    def StatementList(self):
        statementList: list = []
        
        while self._lookahead != None:
            if self._lookahead["type"] == "}":
                break
            statementList.append(self.Statement())
        
        return statementList

    # Statement : VariableDeclaration
    def Statement(self):
        match self._lookahead["type"]:
            case "INIT_STRUCT": return self.InitStruct()
            case  "NEW_STRUCT": return self.NewStruct()
            case             _: return self.VariableDeclaration()
    
    # InitStruct : INIT_STRUCT '{' StatementList '}'
    def InitStruct(self) -> dict:
        self._eat("INIT_STRUCT")
        self._eat("{")
        name: str = self.StructName()
        params: dict = self.StructParameters()
        target: dict = self.StructTarget()
        self._eat("}")

        return {
            "type": "MAIN_STRUCT",
            "name": name,
            "parameters": params,
            "target": target
        }
    
    def StructName(self):
        self._eat("STRUCT_NAME")
        self._eat("DECLARATOR_OPERATOR")
        name = self.Expression()
        return name["value"]
    
    def StructParameters(self):
        self._eat("STRUCT_PARAMS")
        self._eat("DECLARATOR_OPERATOR")
        self._eat("{")
        declarations: dict = self.StatementList()
        self._eat("}")
        return declarations

    def StructTarget(self):
        self._eat("STRUCT_TARGET")
        self._eat("DECLARATOR_OPERATOR")
        self._eat("{")
        declarations: dict = self.VariableDeclaration()
        self._eat("}")
        return declarations
    
    def NewStruct(self):
        self._eat("NEW_STRUCT")
        name = self.Variable()
        self._eat("DECLARATOR_OPERATOR")
        class_type = self.Variable()
        self._eat("{")
        params = self.StatementList()
        self._eat("}")
        return {
            "type": "NEW_STRUCT",
            "name": name["value"],
            "class_type": class_type["value"],
            "declarations": params
        }

    # VariableDeclaration : VariableDeclarator ','
    def VariableDeclaration(self) -> dict:
        declaration: dict = self.VariableDeclarator()
        return {
            "type": "VariableDeclaration",
            "declarations": declaration
        }
    
    # VariableDeclarator : DECLARATOR DECLARATOR_OPERATOR Expression
    def VariableDeclarator(self) -> dict:
        variable = self.Variable()
        self._eat("DECLARATOR_OPERATOR")
        literal = self.Expression()
        return {
            "type": "VariableDeclarator",
            "id": variable,
            "init": literal
        }
    
    # Variable : VARIABLE ;
    def Variable(self):
        token = self._eat("VARIABLE")
        return {
            "type": "Variable",
            "value": token["value"]
        }
    
    # Expression : BinaryExpression ,
    def Expression(self):
        return self.BinaryExpression()
    
    # BinaryExpression | MultiplicativeExpression | MultiplicativeExpression ADDITIVE_OPERATOR MultiplicativeExpression
    def BinaryExpression(self):
        left = self.MultiplicativeExpression()

        while self._lookahead["type"] == "ADDITIVE_OPERATOR":
            operator = self._eat("ADDITIVE_OPERATOR")

            right = self.MultiplicativeExpression()

            left = {
                "type": "BinaryExpression",
                "left": left,
                "operator": operator,
                "right": right
            }

        return left
    
    # MultiplicativeExpression : PrimaryExpression | PrimaryExpression MULTIPLICATIVE_OPERATOR PrimaryExpression
    def MultiplicativeExpression(self):
        left = self.PrimaryExpression()

        while self._lookahead["type"] == "MULTIPLICATIVE_OPERATOR":
            operator = self._eat("MULTIPLICATIVE_OPERATOR")

            right = self.PrimaryExpression()

            left = {
                "type": "BinaryExpression",
                "left": left,
                "operator": operator,
                "right": right
            }
        return left
    
    # PrimaryExpression : ParanthesizedExpression | Literal
    def PrimaryExpression(self):
        match self._lookahead["type"]:
            case "VARIABLE": return self.Variable()
            case "(": return self.ParanthesizedExpression()
            case _: return self.Literal()

    # ParanthesizedExpression : '(' Expression ')'
    def ParanthesizedExpression(self):
        self._eat("(")
        expression = self.Expression()
        self._eat(")")
        return expression
        
    # Literal : NumericLiteral | StringLiteral
    def Literal(self):
        match self._lookahead["type"]:
            case "STRING": return self.StringLiteral()
            case "NUMBER": return self.NumericLiteral()

    # NumericLiteral : NUMBER
    def NumericLiteral(self) -> dict:
        token = self._eat("NUMBER")
        return {
            "type": "NumericLiteral",
            "value": int(token["value"])
        }
    
    # StringLiteral : STRING
    def StringLiteral(self) -> dict:
        token = self._eat("STRING")
        return {
            "type": "StringLiteral",
            "value": token["value"]
        }
    
    def _eat(self, tokenType):
        token = self._lookahead

        if token == None:
            raise SyntaxError(f"Unexpected end of input, expected {tokenType}. At {self._tokenizer._coursor}") 
    
        if token["type"] != tokenType:
            print(self._string[self._tokenizer._coursor], self._tokenizer._coursor, self._lookahead)
            val = token["value"]
            raise SyntaxError(f"Unexpected token {val}, expected {tokenType}. At {self._tokenizer._coursor}")
        
        self._lookahead = self._tokenizer.getNextToken()

        return token
